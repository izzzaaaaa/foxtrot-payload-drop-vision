import cv2
import numpy as np
from markerconfig import LOWER_HSV, UPPER_HSV

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
MIN_AREA = 800
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_h, frame_w = frame.shape[:2]
    frame_center = (frame_w // 2, frame_h // 2)

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #open close
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

                # Draw crosshair on the marker's centroid
                cv2.drawMarker(frame, (cx, cy), (0, 255, 0), markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)
                cv2.putText(frame, f"({cx}, {cy})", (cx + 15, cy - 15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    # Draw frame center reference (a different color so you can visually compare)
    cv2.drawMarker(frame, frame_center, (0, 0, 255),markerType=cv2.MARKER_CROSS, markerSize=20, thickness=2)

    cv2.imshow("Centroid Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()