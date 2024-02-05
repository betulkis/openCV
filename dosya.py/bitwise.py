AND, OR, XOR ve NOT 
import cv2 as cv
import numpy as np

# 400x400 boyutlarında siyah bir boş görüntü oluştur
blank = np.zeros((400, 400), dtype='uint8')

# Beyaz renkte bir dikdörtgen oluştur (rectangle)
rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)

# Beyaz renkte bir daire oluştur (circle)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

# Dikdörtgen ve daireyi göster
cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

# AND  kesişen bölgeler
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# OR  kesişen ve kesişmeyen bölgeler
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# XOR kesişmeyen bölgeler
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# NOT dairenin  tamamının tersi
bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

# Bir tuşa basılmasını bekleyerek pencereleri kapatır
cv.waitKey(0)
