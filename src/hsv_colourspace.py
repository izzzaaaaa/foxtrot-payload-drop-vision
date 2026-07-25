import cv2
import numpy as np

cap = cv2.VideoCapture(0) #opens default webcam
while True:
    ret, frame = cap.read() #grabbing frame by frame
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #converting to HSV color space

    combined = np.hstack((frame, hsv)) #stacking original and HSV images horizontally
    cv2.imshow("BGR(left) vs HSV(right)", combined)

    if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
        break

cap.release() #free webcam
cv2.destroyAllWindows()