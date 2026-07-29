import cv2
import numpy as np
from markerconfig import LOWER_HSV, UPPER_HSV   

cap = cv2.VideoCapture(0)
kernel = np.ones((5,5),np.uint8) #5x5 block for scanning img
min_area = 500 #smaller than this ignored

while True:
    ret,frame =cap.read()
    if not ret:
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, LOWER_HSV, UPPER_HSV)
    cleaned = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) #removes noise
    cleaned = cv2.morphologyEx(cleaned, cv2.MORPH_CLOSE, kernel) #fills the holes

                                            #only outer bound       only corner pts
    contours, _= cv2.findContours(cleaned, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if contours:
        largest = max(contours, key=cv2.contourArea) #b4 comparing run through key
        #picking largest blob
        area = cv2.contourArea(largest) #finds acc num
        if area > min_area:
            x,y,w,h = cv2.boundingRect(largest) #converts contour to rect
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2) 
            #draw box and label
            cv2.putText(frame, f"Area: {area}", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

        cv2.imshow("Contours", frame)
        cv2.imshow("Cleaned mask", cleaned)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()