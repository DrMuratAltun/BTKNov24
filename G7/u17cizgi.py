import cv2 as cv

img=cv.imread(r'data/monalisa.jpg')

cv.imshow('orijinal',img) #görseli göster
print(img.shape[:2])

cv.line(img,(0,0),(534,720), (0,0,255),thickness=3)
# çizilecek reim görselli, baş koordinat, bitiş koordinatr, çigini rengi, kalınlığı
cv.line(img,(534,0),(0,720), (0,0,255),thickness=3)
cv.putText(img,"Fake Mona Lisa", (150,370),
           cv.FACE_RECOGNIZER_SF_FR_COSINE,
           1,(255,0,0),1) #font büyüklüğü, rengi, fırça kalınlığı

cv.imshow('cizgi',img) #görseli göster
cv.waitKey(0)
cv.destroyAllWindows()