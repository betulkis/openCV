resmi gri tona dönüştürür

# Converting to grayscale
renkli görüntüyü (BGR renk formatında) gri tonlamalı bir görüntüye dönüştürür
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
----
cv.cvtColor(), OpenCV kütüphanesinde renk dönüştürme işlemleri için kullanılan bir fonksiyondur.
img: Dönüştürülecek olan renkli görüntü.
cv.COLOR_BGR2GRAY: Renk dönüşüm tipini belirtir. Bu durumda, BGR formatındaki renkleri gri tonlamalı renklere dönüştürmek için cv.COLOR_BGR2GRAY kullanılır.
cv.imshow('Gray', gray):

cv.imshow(), OpenCV kütüphanesinde bir pencerede görüntü göstermek için kullanılan bir fonksiyondur.
'Gray': Pencerenin adı.
gray: Gri tonlamalı görüntü
-----------
# Blur 
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
----
# Görüntüde bulunan kenarları çizer
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny Edges', canny)

aşağıdaki bulanıklık filtresi uygulanmış bir görüntü üzerinde yapılır.
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

------
# Dilating the image görüntüyü genişletme

dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

cv.dilate(), OpenCV kütüphanesinde morfolojik genişletme işlemi yapmak için kullanılan bir fonksiyondur.
canny: Kenar tespiti uygulanmış olan görüntü (Canny kenar tespiti sonucu).
(7, 7): Genişletme çekirdeğinin boyutu
iterations=3: Genişletme işleminin kaç kez tekrarlanacağını belirten parametre. Bu durumda, 3 tekrar yapılır.
-----
# Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)

enişletilmiş görüntü üzerinde erode uygulanarak nesneler küçültülür veya ayrıştırılır. burda eski haline döner
--------
# Resize  yeniden boyutlandır

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

img: Boyutlandırılacak olan orijinal görüntü.
(500, 500): Yeni boyutlar. Bu durumda, genişlik ve yükseklik sırasıyla 500 piksel olarak belirlenmiştir.
interpolation=cv.INTER_CUBIC: Boyutlandırma işlemi sırasında kullanılan interpolasyon yöntemi. Bu durumda, Kübik interpolasyon yöntemi (cv.INTER_CUBIC) kullanılır. Kübik interpolasyon, daha pürüzsüz bir görüntü boyutlandırma sağlar.

-------
# Cropping kırpma

cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)


Bu kod, bir görüntüden belirli bir bölgeyi (kesim) çıkarmak için "cropping" işlemi uygular. İşte bu kodun adım adım açıklaması:

img[50:200, 200:400]:

Görüntü üzerinde bir dilimleme işlemi yapılır.
50:200: Yükseklik (satır) indeksleri aralığı. Bu durumda, 50'den (dahil) 200'e (hariç) kadar olan satırları seçer.
200:400: Genişlik (sütun) indeksleri aralığı. Bu durumda, 2
00'den (dahil) 400'e (hariç) kadar olan sütunları seçer.
bu  kod orijinal görüntüden belirli bir bölgeyi (50-200 yükseklik, 200-400 genişlik) keser ve bu kesilmiş bölgeyi "Cropped" adlı pencerede ekranda gösterir.
