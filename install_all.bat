@echo off
echo ================================
echo  Installing required libraries...
echo ================================

REM ---- Path to Python 3.9 ----
set PY39="C:\Users\anand\AppData\Local\Programs\Python\Python39\python.exe"

echo.
echo 📌 Using Python at: %PY39%
echo.

echo --------------------------------
echo 🔧 Installing PyCAW + comtypes...
echo --------------------------------
%PY39% -m pip install pycaw==20181226 comtypes --upgrade

echo --------------------------------
echo 🔧 Installing OpenCV...
echo --------------------------------
%PY39% -m pip install opencv-python --upgrade

echo --------------------------------
echo 🔧 Installing MediaPipe...
echo --------------------------------
%PY39% -m pip install mediapipe --upgrade

echo --------------------------------
echo 🔍 Checking installations...
echo --------------------------------
%PY39% - <<EOF
try:
    import pycaw
    print("✔ PyCAW OK")
except Exception as e:
    print("❌ PyCAW error:", e)

try:
    import cv2
    print("✔ OpenCV OK")
except Exception as e:
    print("❌ OpenCV error:", e)

try:
    import mediapipe
    print("✔ MediaPipe OK")
except Exception as e:
    print("❌ MediaPipe error:", e)

EOF

echo --------------------------------
echo ▶ Running volumecontroller.py ...
echo --------------------------------
%PY39% "%cd%\volumecontroller.py"

echo.
echo 🎉 DONE!
pause
