# 🎮 Hand Gesture Rock–Paper–Scissors Game

A real-time Rock–Paper–Scissors game controlled using hand gestures, built using Computer Vision and a webcam.

---

## ✨ Project Overview
This is a touchless game where the player uses hand gestures to play against the computer.  
The system captures live video, detects hand landmarks, recognizes gestures, and determines the winner automatically.

This project demonstrates:
- Real-time computer vision
- Gesture recognition
- Human–computer interaction

---

## 🔑 Features
- ✔ Real-time hand detection using webcam  
- ✔ Hand landmark tracking with high accuracy  
- ✔ Gesture recognition:
  - ✊ Rock  
  - ✋ Paper  
  - ✌️ Scissors  
- ✔ Computer opponent (random moves)  
- ✔ Automatic result evaluation (Win / Lose / Draw)  
- ✔ Countdown-based gameplay  
- ✔ Score tracking (Best of 3)  
- ✔ Clean and interactive UI  

---

## 🛠️ Tech Stack
- 🐍 Python  
- 📷 OpenCV – Webcam handling & visualization  
- ✋ MediaPipe – Hand landmark detection  
- 🧠 Computer Vision – Gesture recognition logic  

---

## 🧠 How It Works

1. **Webcam Capture**  
   OpenCV captures real-time video frames.

2. **Hand Detection**  
   MediaPipe detects hand landmarks.

3. **Gesture Recognition**  
   Finger positions are analyzed to classify:
   - Rock  
   - Paper  
   - Scissors  

4. **Game Logic**  
   Computer generates a random move and compares results.

5. **Display Output**  
   Player move, computer move, and result are shown in real-time.

---

## 🖐️ Hand Gesture Mapping

| Gesture | Meaning |
|--------|--------|
| ✊ Closed Fist | Rock |
| ✋ Open Palm | Paper |
| ✌️ Two Fingers | Scissors |

👉 Hold the gesture steady for **3 seconds** to register a move.

---

## ▶️ Installation & Run

```bash
pip install -r requirements.txt
py -3.10 rps_game.py
