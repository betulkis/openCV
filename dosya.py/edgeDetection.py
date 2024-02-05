 gri tonlamalı görüntü üzerinde Laplacian, Sobel ve Canny kenar tespiti 

cv.Laplacian fonksiyonu, gri tonlamalı bir görüntüyü alır ve Laplacian filtresini uygular.
Ardından, sonuç cv.CV_64F veri tipine dönüştürülür ve mutlak değer alınarak negatif değerler ortadan kaldırılır.



Sobel filtresi, görüntüdeki kenarları tespit etmek için bir türev filtresidir. X ve Y yönlere göre türevleri hesaplanır ve ardından bu türevler birleştirilir.
cv.Sobel fonksiyonu, X ve Y yönlere göre türevleri hesaplar.
cv.bitwise_or ile Sobel türevleri birleştirilir.
Sobel filtreleme sonuçları ayrı ayrı 'Sobel X' ve 'Sobel Y' başlıkları altında gösterilir. Ayrıca, birleştirilmiş hali de 'Combined Sobel' başlığı altında gösterilir.



Canny kenar tespiti algoritması, görüntüdeki kenarları bulmak için bir dizi adımdan geçer.
cv.Canny fonksiyonu, belirli bir eşik değerine göre kenarları tespit eder.

canny sobeli aşamalarından birinde kullanan daha gelişmiş bir algoritmadır

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel 
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', canny)
cv.waitKey(0)
