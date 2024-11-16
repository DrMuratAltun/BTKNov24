import cv2 as cv
import numpy as np

# Rastgele bir görüntü oluştur
#img = np.zeros((500, 500, 3), dtype=np.uint8)
img=cv.imread(r'data/monalisa.jpg')
# Yazı ve boyut bilgileri
text = "Fake Mona Lisa"
font = cv.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_thickness = 1
text_color = (255, 0, 0)  # Mavi
background_color = (255, 255, 255)  # Beyaz

# Yazının boyutlarını al
(text_width, text_height), baseline = cv.getTextSize(text, font, font_scale, font_thickness)

# Yazının konumu
x, y = 150, 370
text_start = (x, y)
text_end = (x + text_width, y - text_height - baseline)

# Arka plan dikdörtgeni çiz
cv.rectangle(img, (x, y - text_height - baseline), (x + text_width, y + baseline), background_color, -1)

# Yazıyı ekle
cv.putText(img, text, (x, y), font, font_scale, text_color, font_thickness)

# Görüntüyü göster
cv.imshow("Image", img)
cv.waitKey(0)
cv.destroyAllWindows()
