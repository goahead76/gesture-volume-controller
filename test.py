import cv2

for i in range(3):
    cap = cv2.VideoCapture(i)
    print(f"Trying camera index {i}:", cap.isOpened())
    if cap.isOpened():
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame")
                break
            cv2.imshow(f"Camera {i}", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
        break
