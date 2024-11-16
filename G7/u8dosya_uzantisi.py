import cv2 as cv

img=cv.imread(r'data/satranc3x3.jpg')

b,g,r=cv.split(img)

img_mavi=cv.merge((r,g,b))

cv.imwrite('data/satranc3x3_mavi.png',img_mavi)
cv.imwrite('data/satranc3x3_mavi.jpeg',img_mavi)

#BGR to RGB
img_rgb=cv.cvtColor(img_mavi,cv.COLOR_BGR2RGB)

