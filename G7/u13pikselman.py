import cv2 as cv
import numpy as np

img=cv.imread(r'data/yesil_elma.jpg')

height,width=img.shape[:2]
print("Genişlik ve yükseklik", width,height)
kare_boyut=100
baslangic_x=(width//2)-(kare_boyut//2)
baslangic_y=(height//2)-(kare_boyut//2)

for y in range(baslangic_y,baslangic_y+kare_boyut):
    for x in range(baslangic_x,baslangic_x+kare_boyut):
        img[y,x]=[255,0,0]

cv.imshow('resim',img) #görseli göster
cv.waitKey(0)
cv.destroyAllWindows()