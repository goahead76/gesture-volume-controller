import cv2
import mediapipe as mp
import numpy as np
import time
import math
import platform

# =============================
# VOLUME CONTROL (PYCAW)
# =============================
volume_control_enabled = False
try:
    if platform.system() == "Windows":
        from ctypes import cast, POINTER
        from comtypes import CLSCTX_ALL
        from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        vol_range = volume.GetVolumeRange()
        min_vol, max_vol, _ = vol_range
        volume_control_enabled = True
        print("✔ Volume control initialized")

    else:
        print("❌ Not running on Windows. Volume control disabled.")
except Exception as e:
    print("❌ Volume control error:", e)

# =============================
# MEDIAPIPE HANDS
# =============================
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7, min_tracking_confidence=0.7)

# =============================
# CAMERA START
# =============================
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Error: Could not open camera.")
    exit()

print("✔ Camera started successfully")

pTime = 0

while True:
    success, img = cap.read()
    if not success:
        print("❌ Failed to read frame")
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            h, w, _ = img.shape
            for id, lm in enumerate(handLms.landmark):
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((id, cx, cy))

            # Thumb (4) and Index Finger (8)
            x1, y1 = lm_list[4][1], lm_list[4][2]
            x2, y2 = lm_list[8][1], lm_list[8][2]

            cv2.circle(img, (x1, y1), 8, (255, 0, 255), cv2.FILLED)
            cv2.circle(img, (x2, y2), 8, (255, 0, 255), cv2.FILLED)
            cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Distance between fingers
            length = math.hypot(x2 - x1, y2 - y1)

            # Map distance to volume
            if volume_control_enabled:
                vol = np.interp(length, [20, 220], [min_vol, max_vol])
                volume.SetMasterVolumeLevel(vol, None)

            # Draw distance circle
            mid_x, mid_y = (x1 + x2) // 2, (y1 + y2) // 2
            cv2.circle(img, (mid_x, mid_y), 8, (0, 255, 0), cv2.FILLED)

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if cTime != pTime else 0
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("Hand Volume Controller", img)

    # Exit on Q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

cap.release()
cv2.destroyAllWindows()
