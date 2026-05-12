# =========================================================
# 🌸 ORCAOS v1.0 — PORTFOLIO EDITION
# RTOS-Inspired AI Runtime Environment
# =========================================================
#
# FEATURES
# ✨ Cyberpunk pink-glow UI
# ✨ Live gesture detection
# ✨ RTOS-inspired event queue
# ✨ Concurrent workers
# ✨ Live FPS monitor
# ✨ Embedded-system architecture simulation
#
# INSTALL:
# pip install textual mediapipe opencv-python numpy
#
# RUN:
# python app.py
#
# =========================================================

from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static, Log
from textual.containers import Container

import threading
from queue import Queue
import time

import cv2
import mediapipe as mp


# =========================================================
# GLOBAL STATE
# =========================================================

state = {
    "gesture": "NONE",
    "fps": 0,
    "runtime": "ONLINE",
    "queue": "ACTIVE",
    "threads": "RUNNING",
    "events": 0,

    "ai_output": """
╭──────────────────────────────╮
│        ORCA AI CORE         │
╰──────────────────────────────╯

Waiting for gesture events...

Embedded runtime initialized.
Queue synchronization stable.
"""
}

event_queue = Queue()


# =========================================================
# MEDIAPIPE
# =========================================================

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)


# =========================================================
# GESTURE DETECTION
# =========================================================

def detect_gesture(hand_landmarks):

    tips = [8, 12, 16, 20]

    fingers_up = 0

    for tip in tips:

        if (
            hand_landmarks.landmark[tip].y
            <
            hand_landmarks.landmark[tip - 2].y
        ):
            fingers_up += 1

    if fingers_up >= 3:
        return "OPEN_HAND"

    return "FIST"


# =========================================================
# CAMERA WORKER
# =========================================================

def camera_worker():

    cap = cv2.VideoCapture(0)

    previous_time = time.time()

    last_event = 0

    while True:

        success, frame = cap.read()

        if not success:
            continue

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        results = hands.process(rgb)

        current_time = time.time()

        fps = 1 / (current_time - previous_time)

        previous_time = current_time

        state["fps"] = int(fps)

        if results.multi_hand_landmarks:

            for hand_landmarks in results.multi_hand_landmarks:

                gesture = detect_gesture(
                    hand_landmarks
                )

                state["gesture"] = gesture

                if time.time() - last_event > 2:

                    event_queue.put(
                        ("gesture", gesture)
                    )

                    last_event = time.time()


# =========================================================
# AI RESPONSE ENGINE
# =========================================================

def generate_ai_response(gesture):

    if gesture == "OPEN_HAND":

        state["ai_output"] = f"""
╭──────────────────────────────╮
│        ORCA AI CORE         │
╰──────────────────────────────╯

Gesture accepted.

Concurrent workers synchronized.
Embedded reasoning engine active.
Runtime integrity: STABLE

Live FPS: {state["fps"]}
Events Processed: {state["events"]}
"""

    elif gesture == "FIST":

        state["ai_output"] = """
╭──────────────────────────────╮
│        ORCA AI CORE         │
╰──────────────────────────────╯

Emergency cleanup initiated.

System logs flushed.
Queue reset complete.
"""


# =========================================================
# TEXTUAL APP
# =========================================================

class OrcaOS(App):

    TITLE = "🌸 OrcaOS v1.0"

    CSS = """

    Screen {
        background: #05010a;
        color: #ffd6f2;

        layout: grid;
        grid-size: 2 2;

        grid-columns: 1fr 1fr;
        grid-rows: 1fr 1fr;

        grid-gutter: 1;
        padding: 1;
    }

    Header {
        background: #ff1493;
        color: black;
        text-style: bold;
    }

    Footer {
        background: #ff1493;
        color: black;
    }

    #system_panel {
        border: round #ff1493;
        background: #0d0614;
        color: #ffd6f2;

        padding: 1;
        height: 100%;
    }

    #gesture_panel {
        border: round #ff66cc;
        background: #0d0614;
        color: #ffd6f2;

        padding: 1;
        height: 100%;
    }

    #ai_panel {
        border: round #ff1493;
        background: #0d0614;
        color: #ffd6f2;

        padding: 1;
        height: 100%;
    }

    #log_panel {
        border: round #ff66cc;
        background: #120818;
        color: #ffd6f2;

        height: 100%;
    }

    Static {
        color: #ffd6f2;
        text-style: bold;
    }

    """

    # =====================================================
    # LAYOUT
    # =====================================================

    def compose(self) -> ComposeResult:

        yield Header()

        yield Static("", id="system_panel")

        yield Static("", id="gesture_panel")

        yield Static("", id="ai_panel")

        yield Log(id="log_panel")

        yield Footer()

    # =====================================================
    # STARTUP
    # =====================================================

    def on_mount(self):

        self.logs = self.query_one(
            "#log_panel",
            Log
        )

        self.logs.write_line(
            "[BOOT] Initializing OrcaOS..."
        )

        self.logs.write_line(
            "[WORKER] Camera thread online."
        )

        self.logs.write_line(
            "[QUEUE] Runtime dispatcher active."
        )

        threading.Thread(
            target=camera_worker,
            daemon=True
        ).start()

        self.set_interval(
            0.15,
            self.refresh_ui
        )

        self.set_interval(
            0.15,
            self.process_events
        )

    # =====================================================
    # REFRESH UI
    # =====================================================

    def refresh_ui(self):

        system_text = f"""
╔══════════════════════════════╗
║        ORCAOS RUNTIME       ║
╚══════════════════════════════╝

STATUS        : {state["runtime"]}
FPS           : {state["fps"]}
QUEUE BUS     : {state["queue"]}
THREADS       : {state["threads"]}
EVENTS        : {state["events"]}

ARCHITECTURE:
RTOS-inspired concurrent runtime
"""

        gesture_text = f"""
╔══════════════════════════════╗
║       SENSOR CHANNEL        ║
╚══════════════════════════════╝

CURRENT INPUT:

{state["gesture"]}

LIVE EVENT STREAM:
ACTIVE

WEBCAM SENSOR:
CONNECTED
"""

        self.query_one(
            "#system_panel",
            Static
        ).update(system_text)

        self.query_one(
            "#gesture_panel",
            Static
        ).update(gesture_text)

        self.query_one(
            "#ai_panel",
            Static
        ).update(state["ai_output"])

    # =====================================================
    # EVENT SYSTEM
    # =====================================================

    def process_events(self):

        while not event_queue.empty():

            event_type, value = event_queue.get()

            state["events"] += 1

            self.logs.write_line(
                f"[EVENT] {event_type} -> {value}"
            )

            generate_ai_response(value)

            if value == "OPEN_HAND":

                self.logs.write_line(
                    "[AI] Embedded reasoning triggered."
                )

                self.logs.write_line(
                    "[QUEUE] Event dispatched."
                )

            elif value == "FIST":

                self.logs.clear()

                self.logs.write_line(
                    "[SYSTEM] Runtime cleanup complete."
                )


# =========================================================
# MAIN
# =========================================================

if __name__ == "__main__":

    OrcaOS().run()
