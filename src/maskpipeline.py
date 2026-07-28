import cv2
import numpy as np
from markerconfig import LOWER_HSV, UPPER_HSV   

cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8) #5x5 block for scanning img

while True:
    ret, frame = cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV) #masks markers colour range
    
    
    cv2.imshow("Raw mask", mask)
    cv2.imshow("Cleaned mask", cleaned)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break