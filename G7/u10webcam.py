import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    ret,frame=cap.read()
    gray_frame=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    hvs_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    rgb_frame=cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    flipped_img=cv.flip(frame,-1) 
    ##0 dikey çevirme, 1 yatay, -1 de tersine

    cv.imshow('Webcam',frame)
    cv.imshow('Webcam gri',hvs_frame)
    cv.imshow('RGB',rgb_frame)
    cv.imshow('Flipped Frame',flipped_img)



    if cv.waitKey(1)==ord('q'):
        break