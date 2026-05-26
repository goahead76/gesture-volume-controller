# Gesture Volume Controller Setup Guide

1. Install Python 3.11

   * Download Python 3.11 from official Python website
   * While installing check "Add Python to PATH"

2. Verify Python Installation
   Command:
   py -0

3. Create Virtual Environment
   Command:
   py -3.11 -m venv venv

4. Activate Virtual Environment (PowerShell)
   Command:
   .\venv\Scripts\Activate.ps1

5. Install Required Libraries

   Commands:
   pip install opencv-python
   pip install mediapipe
   pip install pycaw
   pip install comtypes
   pip install numpy

6. Run Project
   Command:
   python volumecontroller.py

# Technologies Used

* Python 3.11
* OpenCV
* MediaPipe
* NumPy
* Pycaw
* Comtypes

# Purpose of Libraries

* OpenCV → webcam and image processing
* MediaPipe → hand tracking
* NumPy → calculations
* Pycaw → system volume control
* Comtypes → Windows audio interface support
