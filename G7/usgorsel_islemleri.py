import cv2 as cv
#görseli nump dizisi şeklinde oku
img=cv.imread('data/satranc3x3.jpg')

#numpyu dizisi şeklinde yazdır
print(img)

cv.imshow('resim',img) #görseli göster
cv.waitKey(0)
cv.destroyAllWindows()