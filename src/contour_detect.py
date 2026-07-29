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
    