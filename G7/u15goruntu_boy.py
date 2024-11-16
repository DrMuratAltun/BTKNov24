import cv2 as cv
img=cv.imread(r'data/yesil_elma.jpg')
cv.imshow('original',img) #görseli göster

fx,fy=0.5,0.5

resized_img=cv.resize(img,None,fx=fx,fy=fy)

cv.imshow('resized',resized_img) #görseli göster

cv.waitKey(0)   
cv.destroyAllWindows()