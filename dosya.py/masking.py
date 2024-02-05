Maskeleme, bir görüntüde belirli bir bölgeyi seçmek veya belirli bir bölgeyi işlemek için kullanılan bir tekniktir. Bu işlem genellikle bir maske adı verilen siyah-beyaz bir görüntü ile gerçekleştirilir. 
Siyah-beyaz bir maske oluşturulur. Bu maske, belirli bir bölgeyi seçmek için kullanılır. Beyaz renk, seçilecek bölgeyi temsil eder.
bir daire şeklinde bir maske oluşturarak bu maskeyi bir görüntüye uygularsan sonuçta sadece dairenin olduğu bir bölge belirgin hale gelir ve diğer bölgeler siyah kalır. 

# Siyah-beyaz maske oluştur
mask = np.zeros_like(img)

# Maskeyi belirli bir bölgeye uygula (örneğin, ortadaki bir daire)
cv.circle(mask, (150, 150), 100, 255, -1)


...
cv.imshow('Weird Shape', weird_shape): Oluşturulan kesişim görüntüsünü ekranda 'Weird Shape' adıyla gösterir.

cv.bitwise_and(img,img,mask=weird_shape): Orijinal resim ile kesişim görüntüsü arasında maskeleme işlemi gerçekleştirir. Yani, sadece kesişen bölge orijinal renk değerlerini korur, diğer bölgeler siyah olur.
