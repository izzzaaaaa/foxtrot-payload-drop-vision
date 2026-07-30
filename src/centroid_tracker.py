import cv2
import numpy as np
from marker_config import LOWER_HSV, UPPER_HSV

cap = cv2.VideoCapture(0)
kernel = np.ones((5, 5), np.uint8)
MIN_AREA = 800
while True:
    ret, frame = cap.read()
    if not ret:
        break