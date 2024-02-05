Kontur Algılama

import cv2 as cv
import numpy as np

# Görüntüyü oku
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Cats', img)

# Siyah bir boş görüntü oluştur
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

# Görüntüyü gri tonlama çevir
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Görüntüyü yumuşat (blurla)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Canny kenar algılama uygula
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Konturları bul
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

# Konturları siyah bir görüntü üzerine çiz
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow('Contours Drawn', blank)

# Pencere kapatmak için bir tuş bekler
cv.waitKey(0)



cv.RETR_LIST: Tüm konturları listeler.
cv.CHAIN_APPROX_SIMPLE: Konturun sadece başlangıç ve bitiş noktalarını saklar.
print(f'{len(contours)} contour(s) found!'):

Bulunan kontur sayısını ekrana yazdırır.
cv.drawContours(blank, contours, -1, (0, 0, 255), 1):

Siyah boş görüntü üzerine bulunan konturları çizer.
-1: Tüm konturları çiz demektir.
(0, 0, 255): Kontur çizim rengi (BGR formatında, bu durumda kırmızı renk).
1: Çizgi kalınlığı.
cv.imshow('Contours Drawn', blank):
Çizilen konturlu görüntüyü "Contours Drawn" adlı pencerede gösterir.





