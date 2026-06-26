# Gesture-Controlled Virtual Puzzle Game 

A real-time virtual puzzle game controlled using hand gestures via webcam. The project uses computer vision to allow drag-and-drop interaction without a mouse or keyboard.

Built using **OpenCV**, **MediaPipe**, and **cvzone**.

---

## Features

- Real-time hand tracking using webcam
- Pinch gesture-based dragging system
- Multiple puzzle pieces (image-based)
- Snap-to-position puzzle mechanics
- Locked pieces after correct placement
- Smooth real-time interaction

---
## Demo GIF

![Demo](Assets/demo.gif)

---

## How It Works

- Webcam captures live video feed
- MediaPipe detects hand landmarks
- Index finger is used as cursor
- Pinch gesture selects and drags puzzle pieces
- Pieces automatically snap into correct positions when close enough

---

## Tech Stack

- Python
- OpenCV
- MediaPipe
- cvzone (HandTrackingModule)

---

## Installation

Install required dependencies:


pip install opencv-python
pip install mediapipe
pip install cvzone
