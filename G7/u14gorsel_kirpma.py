import cv2 as cv

img=cv.imread(r'data/yesil_elma.jpg')

cv.imshow('resim',img) #görseli göster

h,w=img.shape[:2]

start_row,start_col=int(h*0.25),int(w*0.25)
end_row,end_col=int(h*0.75),int(w*0.75)

#resmi kırp

cropped_img=img[start_row:end_row,start_col:end_col]

cv.imshow('Kırpılmış resim',cropped_img) #görseli göster

cv.waitKey(0)
cv.destroyAllWindows()