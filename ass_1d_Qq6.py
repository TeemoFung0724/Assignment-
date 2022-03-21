import cv2
import numpy as np

cam = cv2.VideoCapture(0)

EVT=0
st_po=(0,0)
R=0
L=0

def draw_rectangle(event,x,y,flags,param):
    global EVT
    global PNT
    if event == cv2.EVENT_LBUTTONDOWN:
        EVT = cv2.EVENT_LBUTTONDOWN
        PNT = (x, y)
    if event == cv2.EVENT_LBUTTONUP:
        EVT = cv2.EVENT_LBUTTONUP
        PNT = (x, y)
    if event == cv2.EVENT_RBUTTONDOWN:
        EVT = cv2.EVENT_RBUTTONDOWN
    if event == cv2.EVENT_RBUTTONUP:
        EVT = cv2.EVENT_RBUTTONUP
        cv2.destroyWindow('image_ROX')

while True:
    _, img=cam.read()
    cv2.putText(img, 'MBS3523 Assignment 1b-Q6 Name: Fung Man Yuk', (20, 40), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 0.75,
                (255, 247, 0), 2)
    cv2.imshow('MBS3523',img)
    cv2.setMouseCallback('MBS3523', draw_rectangle)

    if EVT == cv2.EVENT_LBUTTONDOWN:
        st_po=PNT

    if EVT == cv2.EVENT_LBUTTONUP:
        cv2.rectangle(img, st_po, PNT, (255, 247, 0), 3)
        imgBound = img[st_po[1]:PNT[1], st_po[0]:PNT[0]]
        cv2.imshow('ROI', imgBound)
        L=1

    if EVT == cv2.EVENT_RBUTTONDOWN:
        R=1

    if EVT == cv2.EVENT_RBUTTONUP & R==1:
        if L==1:
            L=0
        img = imgOriginal
        R=0

    cv2.imshow('MBS3523 assQ6', img)

    if cv2.waitKey(1) & 0xff == 27:
            break

capture.release()
cv2.destroyAllWindows()