import cv2
import numpy as np

cam = cv2.VideoCapture(0)

def nil(x):
    pass

cv2.namedWindow('MBS3523')
cv2.createTrackbar('X','MBS3523',320,750,nil)
cv2.createTrackbar('Y','MBS3523',240,750,nil)

while True:
    success, img = cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1b-Q5 Name: Fung Man Yuk', (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(255, 247, 0), 2)
    x = cv2.getTrackbarPos('X', 'MBS3523')
    y = cv2.getTrackbarPos('Y', 'MBS3523')
    cv2.line(img,(x,0),(x,750),(255,0,0),6)
    cv2.line(img, (0, y), (750, y), (255, 0, 0), 6)
    cv2.imshow('MBS3523', img)
    if cv2.waitKey(1) & 0xff == 27:
        break

cv2.destroyAllWindows()