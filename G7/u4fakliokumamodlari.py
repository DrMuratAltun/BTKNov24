import cv2 as cv

#gri skala

img_bgr=cv.imread('data/satranc3x3.jpg')
img_gri=cv.imread('data/satranc3x3.jpg',0)

cv.imshow('Normal',img_bgr) #görseli göster
cv.imshow('Gri skala',img_gri) #görseli göster
cv.waitKey(0)
cv.destroyAllWindows()