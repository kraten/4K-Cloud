#!/usr/bin/python36

import cv2

cap = cv2.VideoCapture(0)

ret, frame = cap.read()
cv2.imwrite('./images/users/kb.jpg', frame)

cap.release()
