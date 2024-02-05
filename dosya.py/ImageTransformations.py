# Translation
kaydırma
def translate(img, x, y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

Kaydırma matrisi (transMat) oluşturulur. Bu matris, görüntüyü belirli bir uzaklıkta (x ve y) kaydırmak için kullanılır.
[[1, 0, x], [0, 1, y]]: 2x3 boyutunda bir matris

dimensions = (img.shape[1], img.shape[0]):
Görüntünün boyutları dimensions değişkenine atanır. (genişlik, yükseklik) olarak alınır.

orijinal görüntü (img) -100 birim x ekseni ve 100 birim y ekseni boyunca kaydırılır.
Bu işlem, görüntüyü sol üst yöne doğru 100 piksel yukarıya ve 100 piksel sola kaydırır.

# -x  sol
# -y  yukarı
# x  sağ
# y aşağı

python transformations.py terminalde çalıştır


# Rotation
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width,height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(img, -90)
cv.imshow('Rotated Rotated', rotated_rotated)

cv.waitKey(0)


# Resizing yeniden boyutlandırma
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

cv.flip(img, -1):
cv.flip(), OpenCV kütüphanesinde bir görüntüyü çevirmek için kullanılan bir fonksiyondur.
img: Çevrilecek olan orijinal görüntü.
-1: Çevirme yöntemi. Bu durumda, hem yatay hem de dikey eksende çevirme anlamına gelir.

# Cropping görüntüden belirli bir bölgeyi çıkarmak
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)
