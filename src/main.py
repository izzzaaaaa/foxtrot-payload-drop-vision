import cv2
import numpy as np
from dronekit import connect
from markerconfig import LOWER_HSV, UPPER_HSV

TOLERANCE = 30  #how close Cx Cy must be to frame center
MIN_AREA = 800

print("Connecting to vehicle on: tcp:127.0.0.1:5762")
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
print("Connected. Starting vision feed...")

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_h, frame_w = frame.shape[:2]
    frame_cx, frame_cy = frame_w // 2, frame_h // 2

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(cleaned, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        largest = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest)

        if area > MIN_AREA:
            M = cv2.moments(largest)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])

                cv2.drawMarker(frame, (cx, cy), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)

                offset_x = cx - frame_cx #how far centroid from centre
                offset_y = cy - frame_cy

                if abs(offset_x) < TOLERANCE and abs(offset_y) < TOLERANCE:
                    print(f"DROP TRIGGERED | Cx={cx}, Cy={cy} | Vehicle mode: {vehicle.mode.name}")
                else:
                    print(f"Not aligned | offset_x={offset_x}, offset_y={offset_y}")

    cv2.drawMarker(frame, (frame_cx, frame_cy), (0, 0, 255), markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)
    cv2.imshow("Payload Drop Vision", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
vehicle.close()