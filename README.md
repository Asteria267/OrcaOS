<div align="center">

# ✨ OrcaOS v1.0 ✨

<img src="https://readme-typing-svg.herokuapp.com?font=Orbitron&size=28&duration=3000&color=FF69B4&center=true&vCenter=true&width=900&lines=RTOS-Inspired+AI+Operating+Environment;Gesture+Input+%2B+Local+LLM+Reasoning;Embedded+Systems+Architecture+on+a+Laptop;Built+with+Textual+%2B+Ollama+%2B+MediaPipe" />

<br>

<p align="center">
  <img src="https://img.shields.io/badge/STATUS-SHIPPED-ff69b4?style=for-the-badge&logo=github"/>
  <img src="https://img.shields.io/badge/VERSION-v1.0-ff1493?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/ARCHITECTURE-RTOS_INSPIRED-ff69b4?style=for-the-badge"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-ff69b4?style=flat-square&logo=python"/>
  <img src="https://img.shields.io/badge/Textual-TUI-ff1493?style=flat-square"/>
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-ff69b4?style=flat-square"/>
  <img src="https://img.shields.io/badge/MediaPipe-Gesture_AI-ff1493?style=flat-square"/>
  <img src="https://img.shields.io/badge/OpenCV-Computer_Vision-ff69b4?style=flat-square"/>
</p>

---

### 🌸 “Firmware architecture thinking — running entirely in software.” 🌸

</div>

---

# 🧠 What is OrcaOS?

**OrcaOS** is an RTOS-inspired AI operating environment built entirely in Python.

Instead of bare-metal hardware, OrcaOS treats a laptop like an embedded system:

- webcam → sensor input  
- event queue → task scheduler  
- local LLM → reasoning engine  
- Textual UI → system shell  

The architecture mimics how embedded firmware systems operate:
concurrent tasks, queues, event-driven logic, and real-time updates.

---

# ✨ Features

## 🌷 Gesture-Based Input
MediaPipe-powered hand gesture detection:
- ✋ Open hand → triggers AI reasoning
- ✊ Fist → clears system logs

---

## 🧠 Local AI Inference
Integrated with Ollama for fully local reasoning:
- no cloud APIs
- offline capable
- embedded-AI style architecture

---

## 📡 Live Sensor Stream
Real-time updates from:
- webcam input
- gesture state
- FPS monitoring
- event system

---

## 🖥️ Textual TUI Shell
Interactive terminal UI built with Textual:
- live runtime status
- queue activity
- reasoning output
- embedded-style console logs

---

# 🏗️ Architecture

```text
┌──────────────────────┐
│     SENSOR INPUT     │
│  Webcam / Gestures   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     EVENT QUEUE      │
│  RTOS-style message  │
│       passing        │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      SCHEDULER       │
│ Concurrent Workers   │
└──────────┬───────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐ ┌────────────┐
│ Textual │ │ Local LLM  │
│   TUI   │ │ Reasoning  │
└─────────┘ └────────────┘
```

---

# ⚡ Tech Stack

| Layer | Technology |
|---|---|
| TUI Shell | Textual |
| AI Reasoning | Ollama |
| Computer Vision | MediaPipe |
| Video Input | OpenCV |
| Concurrency | threading |
| Runtime Messaging | Queue |
| Language | Python |

---

# 🚀 Run OrcaOS

## 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Install Ollama

👉 https://ollama.com

Then pull a model:

```bash
ollama pull llama3
```

---

## 3️⃣ Launch OrcaOS

```bash
python app.py
```

---

# 📸 Demo Goals

✅ Single-command launch  
✅ Live TUI environment  
✅ Gesture-controlled runtime  
✅ Local LLM reasoning  
✅ RTOS-inspired architecture  
✅ Event-driven worker system  

---

# 🌌 Why This Project Exists

Modern AI systems are becoming increasingly embedded:
robots, wearables, edge devices, smart environments.

OrcaOS explores the idea of:
> “What if embedded firmware principles merged with local AI reasoning?”

This project simulates that architecture entirely in software.

---

# 🔮 Future Roadmap

## v2.0
- Raspberry Pi Pico port
- physical sensors
- hardware actuators
- ISR simulation
- dedicated scheduler loop
- distributed edge nodes

---

# 💖 Screenshots

> Add your terminal screenshots here after recording.

```md
![demo](YOUR_SCREENSHOT_LINK)
```

---

# 🛠️ Common Fixes

## Textual missing

```bash
pip install textual
```

---

## Ollama not responding

Check:

```bash
ollama run llama3
```

---

## Webcam issues

Close other apps using the camera.

---

# 📦 Release

Current stable release:

## 🌸 `v1.0`

Integrated:
- gesture input
- local AI reasoning
- live event runtime
- Textual shell

---

<div align="center">

# 💗 OrcaOS 💗

### “Embedded systems thinking for AI-native environments.”

<img src="https://capsule-render.vercel.app/api?type=waving&color=ff69b4&height=120&section=footer"/>

</div>
