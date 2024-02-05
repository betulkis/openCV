renk kanalları

import cv2 as cv
import numpy as np

# Görüntüyü oku
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Siyah bir boş görüntü oluştur (sadece genişlik ve yükseklik bilgilerini kullanır)
blank = np.zeros(img.shape[:2], dtype='uint8')

# Renk kanallarını ayır
b, g, r = cv.split(img)

# Blue kanalı ile sadece mavi renkli görüntü oluştur
blue = cv.merge([b, blank, blank])

# Green kanalı ile sadece yeşil renkli görüntü oluştur
green = cv.merge([blank, g, blank])

# Red kanalı ile sadece kırmızı renkli görüntü oluştur
red = cv.merge([blank, blank, r])

# Renkli kanal görüntülerini göster
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

# Görüntünün boyutlarını ve renk kanallarının boyutlarını yazdır
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Renk kanallarını birleştirerek orijinal görüntüyü elde et
merged = cv.merge([b, g, r])
cv.imshow('Merged Image', merged)

# Pencere kapatmak için bir tuş bekleyin
cv.waitKey(0)
