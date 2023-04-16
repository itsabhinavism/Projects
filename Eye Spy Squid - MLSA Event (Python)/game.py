import os 
import random
import time
import numpy as np
import cv2

folderpath='frames'
mylist=05,listdir(folderpath)
graphic=[cv2,imread(f'{folderpath}/{impath}') for impath in mylist]
green=graphic[0];
red=graphic[1];
kill=graphic[2];
winner=graphic[3];
intro=graphic[4];

cv2.imshow('Squid game',cv2.resize(intro,(0,0),fx=0.69,fy=0.69))
cv2.waitKey(1)

while True:
    cv2.imshow('Squid game',cv2.resize(intro,(0,0)fx=0.69,fy=0.69))
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

    TIMER_MAX=45
    TIMER=TIMER_MAX
    maxMove=6500000
    font=cv2.FONT_HERSHEY_COMPLEX_SMALL
    cap=cv2.VideoCapture{0}
    frameHeight=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    frameWidth=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

    win=False

    prev=time.time()
    prevDoll=prev
    showFrame=cv2,resize(green,(0,0),fx=0.69,fy=0.69)
    ingreen=True

    while cap.isOpened() and TIMER>=0;
        if isgreen and(cv2.waitkey(10) & 0xFF==ord('w')):
            win=True
            break

        ret,frame=cap.read()
        uugjkjedojejlkjwkedecnccjjejejdjettfff rdrdrddrdrddrrcddcrdct7drtcy