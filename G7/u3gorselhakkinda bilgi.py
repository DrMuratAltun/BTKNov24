import cv2 as cv
img=cv.imread(r'data/yesil_elma.jpg')

#satır*sütun
print("Yükseklik, Genişlik, kanal sayısı",img.shape)
print("Yükseklik",img.shape[0])
print("Genişlik",img.shape[1])
print("Kanal Sayısı",img.shape[2])

#veri türü
print ('Veri türü', img.dtype)

cv.imshow('resim',img) #görseli göster
cv.waitKey(0)
cv.destroyAllWindows()

