# -*- coding: utf-8 -*-

import numpy as np
import cv2
import sys
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

cap = cv2.VideoCapture((os.getenv('VIDEO_ADREESS') )

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()