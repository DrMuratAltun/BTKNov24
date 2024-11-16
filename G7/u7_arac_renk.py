import cv2 as  cv

img_togg=(r'data/kirmizi_togg.jpg')
img_ferrari=(r'data/kirmizi_ferrari.jpg')

img=cv.imread(img_ferrari)

b,g,r=cv.split(img)

img_mavi=cv.merge((r,g,b))

img_yesil=cv.merge((b,r,g))

img_sari=cv.merge((b,r,r))

img_mk=cv.merge((r,g,r))

cv.imshow('Orijimal',img) #görseli göster
cv.imshow('Mavi',img_mavi) #görseli göster
cv.imshow('Yesil',img_yesil) #görseli göster
cv.imshow('Sarı',img_sari) #görseli göster
cv.imshow('Mor',img_mk) #görseli göster

cv.waitKey(0)
cv.destroyAllWindows()