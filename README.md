
﻿# Face Anonymizer 👤✨

A simple Python project that detects faces in images and blurs them automatically to protect privacy. It uses **OpenCV** and Google's **MediaPipe Tasks API**.

The project automatically adds extra space (padding) around the face to make sure the whole head, including hair and chin, is completely hidden.

---

## 🚀 Features
* **Fast Face Detection:** Uses MediaPipe's BlazeFace model for quick detection.
* **Full Head Blur:** Adds smart padding so the entire face area is covered.
* **Safe Boundaries:** Uses `min` and `max` functions to prevent code crashes if the face is near the edge of the image.

---

## 🛠️ Requirements
Before running the code, you need to install these Python libraries:

```bash
pip install opencv-python mediapip

Note: Make sure to download the blazeface_common.task model file and place it in the main project folder

Bash
python Computer_vision.py
