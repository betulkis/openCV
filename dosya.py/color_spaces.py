
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/boston.jpg')
cv.imshow('boston', img)

plt.imshow(img)
plt.show() 
renklerin ters çevrilmesi 2 kütüphane arasında gerçekleşebilir
matplotlibde bgr görüntüsünü alıp görüntülemek istersek matplotlib bu görüntüyü BGR görüntüsü gibi yapmazz
bu görüntüyü RGB görüntüsüymüş gibi görüntüler(kırmızı mavi mavi kırmızı gibi)
---
import cv2 as cv
img = cv.imread('Photos/boston.jpg')
cv.imshow('boston', img)

# BGR to Grayscale  BGR resim formatından gri tonlamalı formata dönüştürüyoruz.
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
terminalde python spaces.py  yaz

# BGR dan HSV  cırtlak
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR dan L*a*b   soluk
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR dan RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV dan BGR
lab_bgr = cv.cvtColor(lab, cv.COLOR_LAB2BGR)
cv.imshow('LAB --> BGR', lab_bgr)

cv.waitKey(0)  hepsinin sonunda bu hep var
