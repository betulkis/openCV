bulanıklaştırma

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)
---
Averaging (Ortalama Bulanıklık) filtresini uygula
(3,3): Bulanıklık etkisinin boyutunu belirtir.
average = cv.blur(img, (3,3))
Blur uygulanmış görüntüyü göster
cv.imshow('Average Blur', average)
---
python smoothing.py unutma
----
# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)
---
# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)
--
# Bilateral      
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)
filtre uygulandığında görüntü daha net ve kenarlar daha belirgin hale gelir. 
---
cv.waitKey(0)
