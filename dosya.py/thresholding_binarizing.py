bir renkli görüntüyü gri tonlamaya dönüştürdükten sonra, basit thresholding ve adaptif thresholding yöntemlerini uygulayarak farklı ikili görüntüler oluşturmayı amaçlar

import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   #Orijinal renkli resmi gri tonlamaya dönüştürür.
cv.imshow('Gray', gray)

# Simple Thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY )  # !! cv.threshold(gray, 150, 255, cv.THRESH_BINARY): Gri tonlamaya dönüştürülmüş resimdeki piksel değerlerini 150 eşik değeri ile karşılaştırır. 150'den büyük olan pikselleri beyaz (255), küçük olanları siyah (0) yaparak ikili bir görüntü oluşturur.
cv.imshow('Simple Thresholded', thresh)  #ekranda gösterir

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )  # bu sefer, 150'den büyük olan pikselleri siyah (0), küçük olanları beyaz (255) yaparak tersine çevirir.
cv.imshow('Simple Thresholded Inverse', thresh_inv)
------------------------------------------------------------------------
# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)  # pikselin çevresindeki bir bölgenin ortalamasını ve standart sapmasını kullanarak eşik değerini hesaplar
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)
