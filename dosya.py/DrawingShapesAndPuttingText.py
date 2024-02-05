Şekil Çizme ve Metin Koyma
 

# OpenCV kütüphanesini kullanarak bir siyah arkaplanlı boş bir görüntü oluşturmayı ve bu görüntüyü ekranda göstermeyi sağlar
en son python draw.py komutunu gir terminalde
--
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

--
# np.zeros((500, 500, 3), dtype='uint8'): Bu ifade, NumPy kütüphanesini kullanarak bir NumPy dizisi oluşturur. Bu dizi, 500 piksel genişliğinde, 500 piksel yüksekliğinde ve 3 renk kanalına sahip (RGB) bir görüntüyü temsil eder. dtype='uint8' ifadesi, dizinin elemanlarının 8 bitlik işaretsiz tamsayılar olduğunu belirtir, yani her renk kanalındaki piksel değerleri 0 ile 255 arasında olabilir.
#np.zeros((500, 500)): Tek bir renk kanalına sahip, siyah-beyaz bir görüntü.
#np.zeros((500, 500, 3)): Üç renk kanalına sahip, renkli bir görüntü (RGB).
#Bu iki durum arasındaki fark, renkli bir görüntüde her pikselin üç renk bileşeni (RGB) içermesi ve bu nedenle her piksel için üç sayı gerektirmesidir.

# cv.imshow('Blank', blank): Bu ifade, oluşturulan boş görüntüyü ekranda göstermek için OpenCV'nin cv.imshow() fonksiyonunu kullanır. 'Blank' stringi, pencerenin başlığını temsil eder, yani ekranda gösterilen pencerenin adıdır. blank ise gösterilecek olan görüntüdür.

# Bu iki satır kod, genellikle OpenCV üzerinde bir şeyler denemek veya başlangıç ​​olarak bir boş görüntü oluşturmak istediğiniz durumlarda kullanılır. blank adlı boş görüntü üzerine çizimler yapabilir veya başka işlemler uygulayabilirsiniz.
----------------------
# 1. Görüntüyü belirli bir renge boyayın

blank[:] = 0,255,0
cv.imshow('Green', blank)
yeşill ekran açar
--
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

Bu iki satır, önceden oluşturulmuş olan blank adlı boş bir görüntüyü üzerinde belirli bir bölgeye renk eklemeyi ve ardından bu görüntüyü ekranda göstermeyi sağlar. 
blank[200:300, 300:400]: Bu kısım, blank görüntüsündeki bir bölgeyi seçer. Burada, 200'den 300'e kadar olan yükseklik aralığını ve 300'den 400'e kadar olan genişlik aralığını ifade eder.
= 0,0,255: Bu renk atama işlemini yapar. Burada, RGB renk uzayında mavi rengi temsil eden bir renk kodu kullanılır. (0, 0, 255), (B, G, R) sırasına göre kırmızı rengi temsil eder.

#cv.imshow('Green', blank):

Bu ifade, üzerinde renk değişikliği yapılmış olan blank görüntüsünü ekranda gösterir.
'Green': Bu, ekrandaki pencerenin adını temsil eder.

#Bu kod örneği, belirli bir bölgeye (200-300 yükseklik ve 300-400 genişlik aralığı) kırmızı bir renk ekleyerek, bu bölgeyi renklendirmektedir. Renkli bir görüntü kullanıldığı için üç renk kanalı (RGB) bulunur ve bu nedenle (0, 0, 255) kodu kırmızı renge karşılık gelir. cv.imshow() fonksiyonu ile renklendirilmiş görüntüyü ekranda gösterebilirsiniz.

--komple aşağıdaki kod siyah ekranda belirli ölçülerde kırmızı kare oluşturur:

import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

cv.waitKey(0)

---------------------------
# 2. Dikdörtgen rectangle Çizme

cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=2)
cv.imshow('Rectangle', blank)

#bu
başlangıç noktasından 0,0 (açılan pencerenin en sol üst köşesi) 250,250ye kadar giden yeşil dikdçizme

cv.rectangle(), OpenCV kütüphanesinde bir dikdörtgen çizmek için kullanılan bir fonksiyondur.
blank: Dikdörtgenin çizileceği görüntü.
(0,0): Dikdörtgenin sol üst köşesinin koordinatları.
(250,250): Dikdörtgenin sağ alt köşesinin koordinatları.
(0,255,0): Dikdörtgenin rengi. Bu durumda, tam yoğunluğundaki yeşil renk.
thickness=2: Dikdörtgenin kenar kalınlığı. Burada, kalınlığı 2 piksel olarak belirlenmiştir.
cv.imshow('Rectangle', blank):
cv.imshow(), OpenCV kütüphanesinde bir pencerede görüntü göstermek için kullanılan bir fonksiyondur.
----------
thickness=cv.FILLED
ve
thickness=-1  dikdörtgenin içini seçilen renkle doldurur !içi dolu bir dikdörtgen!
--------
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

Bu kod satırı, bir dikdörtgenin sağ alt köşesinin koordinatlarını belirlerken, dikdörtgenin genişliğini ve yüksekliğini blank görüntüsünün yarısına (yarı genişlik ve yarı yükseklik) ayarlamaktadır. Bu yaklaşım, dikdörtgenin boyutunu görüntünün boyutuna göre otomatik olarak ayarlamak ve onu görüntünün ortasına yerleştirmek için kullanılabilir.
---------------------------
# 3. circle daire
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank)

(blank.shape[1]//2, blank.shape[0]//2): Çemberin merkez koordinatları. Burada, çemberin merkezi, blank görüntüsünün genişliğinin yarısı ve yüksekliğinin yarısı olacak şekilde belirlenir. Bu, çemberin görüntünün ortasında olmasını sağlar.
40: Çemberin yarıçapı. Burada, yarıçap 40 piksel olarak belirlenmiştir.
(0,0,255): Çemberin rengi. Bu durumda, tam yoğunluğundaki kırmızı renk.
thickness=-1: Çemberin kenar kalınlığı. Burada, -1 kullanılarak içi dolu bir çember çizilir.
--------------------------
# 4. çizgi line çiz
cv.line(blank, (100,250), (300,400), (255,255,255), thickness=3)
cv.imshow('Line', blank)

(100,250): Çizginin başlangıç noktasının koordinatları.
(300,400): Çizginin bitiş noktasının koordinatları.
(255,255,255): Çizginin rengi. Bu durumda, tam yoğunluğundaki beyaz renk.
thickness=3: Çizginin kalınlığı. Burada, kalınlığı 3 piksel olarak belirlenmiştir.
------------------------
# 5. Write text
cv.putText(blank, 'Hello, my name is Jason!!!', (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)
cv.imshow('Text', blank)

cv.putText(), OpenCV kütüphanesinde bir görüntüye metin eklemek için kullanılan bir fonksiyondur.
blank: Metnin eklenileceği görüntü.
'Hello, my name is Jason!!!': Eklenen metin.
(0, 225): Metnin başlangıç koordinatları. Burada, x=0 ve y=225 olarak belirlenmiştir.
cv.FONT_HERSHEY_TRIPLEX: Kullanılan yazı tipi. Burada en soondaki TRIPLEX fontu kullanılmıştır.

1.0: Yazı boyutu ölçeği. 1.0 normal boyutu temsil eder.
(0, 255, 0): Metnin rengi yeşil renk.
2: Metnin kalınlığı 2


en sona bunu ekle !!!!!!!

cv.waitKey(0)
