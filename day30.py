Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# app.py
# OrcaOS v1.0
# Single-file MVP build
#
# FEATURES:
# - Textual TUI
# - MediaPipe gesture detection
# - Ollama local LLM integration
# - Live FPS/sensor display
# - Queue-based architecture
# - Multi-threaded runtime
#
# RUN:
# pip install textual ollama mediapipe opencv-python numpy
# python app.py

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Log
from textual.containers import Container
from textual.reactive import reactive

import threading
from queue import Queue
import time

import cv2
import mediapipe as mp
import ollama


# =========================================================
# GLOBAL STATE
# =========================================================

state = {
    "gesture": "NONE",
    "fps": 0,
    "llm_output": "Waiting for input...",
    "system_status": "RUNNING",
}

event_queue = Queue()


# =========================================================
# GESTURE WORKER
# =========================================================

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


def detect_gesture(hand_landmarks):
    """
    VERY SIMPLE gesture detection:
    Open hand = all fingers extended
    Fist = default fallback
    """

    tips = [8, 12, 16, 20]
    fingers_up = 0

    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers_up += 1

    if fingers_up >= 3:
        return "OPEN_HAND"

    return "FIST"


def gesture_worker():
    cap = cv2.VideoCapture(0)

    previous_time = time.time()
    last_sent = 0

    while True:
        success, frame = cap.read()

        if not success:
            continue

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb)

        current_time = time.time()

        fps = 1 / (current_time - previous_time)
        previous_time = current_time

        state["fps"] = int(fps)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                gesture = detect_gesture(hand_landmarks)

                state["gesture"] = gesture

                # avoid spamming queue
                if time.time() - last_sent > 3:
                    event_queue.put(("gesture", gesture))
                    last_sent = time.time()


# =========================================================
# OLLAMA
# =========================================================

def ask_llm(prompt):

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        content = response["message"]["content"]

        state["llm_output"] = content[:700]

        return content

    except Exception as e:
        state["llm_output"] = f"OLLAMA ERROR:\n{str(e)}"


# =========================================================
# TEXTUAL APP
# =========================================================

class OrcaOS(App):

    TITLE = "OrcaOS v1.0"

    CSS = """
    Screen {
        layout: grid;
        grid-size: 2 2;
        padding: 1;
    }

    #system_panel {
        border: round green;
        padding: 1;
    }

    #gesture_panel {
        border: round cyan;
        padding: 1;
    }

    #llm_panel {
        border: round magenta;
        padding: 1;
    }

    #log_panel {
        border: round yellow;
        padding: 1;
    }

    Static {
        margin: 1;
    }
    """

    def compose(self) -> ComposeResult:

        yield Header()

        with Container(id="system_panel"):
            yield Static("SYSTEM", id="system_text")

        with Container(id="gesture_panel"):
            yield Static("GESTURE", id="gesture_text")

        with Container(id="llm_panel"):
            yield Static("LLM OUTPUT", id="llm_text")

        with Container(id="log_panel"):
            yield Log(id="logs")

        yield Footer()

    # =====================================================
    # STARTUP
    # =====================================================

    def on_mount(self):

        self.logs = self.query_one("#logs", Log)

        self.logs.write_line("Booting OrcaOS...")
        self.logs.write_line("Initializing workers...")
        self.logs.write_line("Gesture worker online.")

        threading.Thread(
            target=gesture_worker,
            daemon=True
        ).start()

        self.set_interval(0.2, self.refresh_ui)
...         self.set_interval(0.2, self.process_events)
... 
...     # =====================================================
...     # UI REFRESH
...     # =====================================================
... 
...     def refresh_ui(self):
... 
...         system_text = f"""
... [ OrcaOS Runtime ]
... 
... STATUS: {state["system_status"]}
... FPS: {state["fps"]}
... QUEUE: ACTIVE
... THREADS: RUNNING
... """
... 
...         gesture_text = f"""
... [ Gesture Input ]
... 
... CURRENT:
... {state["gesture"]}
... 
... EVENT BUS:
... LIVE
... """
... 
...         self.query_one("#system_text", Static).update(system_text)
... 
...         self.query_one("#gesture_text", Static).update(gesture_text)
... 
...         self.query_one("#llm_text", Static).update(
...             state["llm_output"]
...         )
... 
...     # =====================================================
...     # EVENT PROCESSOR
...     # =====================================================
... 
...     def process_events(self):

        while not event_queue.empty():

            event_type, value = event_queue.get()

            self.logs.write_line(
                f"EVENT -> {event_type}: {value}"
            )

            if event_type == "gesture":

                if value == "OPEN_HAND":

                    self.logs.write_line(
                        "Triggering local reasoning engine..."
                    )

                    threading.Thread(
                        target=ask_llm,
                        args=(
                            "You are the onboard AI of OrcaOS. "
                            "Respond like a futuristic embedded operating system.",
                        ),
                        daemon=True
                    ).start()

                elif value == "FIST":

                    state["llm_output"] = "Logs cleared."

                    self.logs.clear()

                    self.logs.write_line(
                        "SYSTEM LOG RESET"
                    )


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

