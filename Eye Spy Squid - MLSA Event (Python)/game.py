import os #to access frames
import random #to generate random numbers
import time 
import numpy as np #mathematical analysis
import cv2 

folderpath='frames'
mylist=os.listdlr(folderpath)
graphic=[cv2.imread(f'{folderpath}/{impath}') for impath in mylist ] #created a list for frames pic cv2.imread to read images
green=graphic[0]; 
red=graphic[1];
kill=graphic[2];
winner=graphic[3];
intro=graphic[4];

cv2.imshow('Squid game',cv2.resize(intro,(0,0),fx=0.69,fy=0.69)) #imshow opens the opencv screen name Squid Game (0,0) means frame will cover full screen, fx-fy direction of x and y
cv2.waitKey(1) #time for coming to next frame

while True: #so that user doesn't prompt screen doesn't change
    cv2.imshow('Squid Game',cv2.resize(intro,(0,0),fx=0.69,fy=0.69))
    if cv2.waitkey(1) & 0xFF==ord('q'): #end the frame if user press q
        break

TIMER_MAX=45 #min time
TIMER=TIMER_MAX #backup in new variable
maxMove=6500000 #how many times green & red light change 
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cap=cv2.VideoCapture(0) #capture the video from webcam 0 since laptop's cam, 1 for seperate cam
frameHeight=cap.get(cv2.CAP_PROP_FRAME_HEIGHT) 
frameWidth=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

win=False 

prev=time.time()
prevDoll=prev
showFrame=cv2.resize(green,(0,0),fx=0.69,fy=0.69) #game starts with green
isgreen=True

while cap.isOpened() and TIMER>=0: 
    if isgreen and (cv2.waitKey(10) & 0xFF=ord('w')):
        win=True
        break

    ret,frame=cap.read()

    cv2.putText(showFrame,str(TIMER),(50,50),font 1,(0,int(255*(TIMER)/TIMER_MAX)),int(255*(TIMER_MAX-TIMER)/(TIMER_MAX)),4,cv2.LINE_AA)

    cur=time.time()

    no=random.randint(1,5) 
    if cur-prev>=no:
        prev=cur
        TIMER=TIMER-no
        if cv2.waitKey(10) & 0xFF==ord('w'):
            win=True
            break

        if isgreen: #
            showFrame=cv2.resize(red,(0,0),fx=0.69,fy=0.69)
            isgreen=False #Color will become red
            ref=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) 
        else:
            showFrame=cv2.resize(green,(0,0),fx=0.69,fy=0.69) 
            isgreen=True
    if not isgreen:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting img to grayscale
        frameDelta=cv2.absdiff(ref,gray)
        thresh=cv2.threshold(20,255,cv2.THRESH_BINARY)[1] #detect the movement 0 if no movement
        change=np.sum(thresh)