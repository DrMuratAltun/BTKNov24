import cv2 as cv
import numpy as np

#videodan görüntü almak için
input_video=r'data/araba_video.mp4'
cap=cv.VideoCapture(input_video)

#video özellikleri
fourcc=cv.VideoWriter_fourcc(*'mp4v') #kodek
fps=int(cap.get(cv.CAP_PROP_FPS)) #fps
width=int(cap.get(cv.CAP_PROP_FRAME_WIDTH)) #genişlik
height=int(cap.get(cv.CAP_PROP_FRAME_HEIGHT)) #yükseklik

out=cv.VideoWriter('data/yesilvideo.mp4',
                   fourcc,
                   fps,
                   (width,height))

while cap.isOpened():
    ret,frame=cap.read()
    if not ret:
        break

    b,g,r=cv.split(frame)
    rgb_frame=cv.merge((b,r,g))
    cv.imshow('Mavi araba',rgb_frame) #görseli göster
    out.write(rgb_frame)

    if cv.waitKey(1)==ord('q'):
        break

cap.release()
out.release()
cv.destroyAllWindows()   