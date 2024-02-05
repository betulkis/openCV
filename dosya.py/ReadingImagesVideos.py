import cv2 as cv

# resmi açma
img = cv.imread('Photos/cat.jpg')
cv.imshow('cat', img)
cv.waitKey(0)

(kaydet run , terminalde python read.py dediğinde resim açılır)

# reading video
capture = cv.VideoCapture()

(bu yöntem  ya 0123 vb gibi bir tam sayı argümanını ya da bir video dosyasının yolunu alır)

capture = cv.VideoCapture(0) 

( 0  bilgisayarındaki webcam e referans verir 1 bağlanan ilk kameraya ..)

capture = cv.VideoCapture('Videos/dog.mp4')

(bu ise bilgisayarımızdaki dog isimli videoyu açar sonra vşdeo bitince kapanır)

#videonun sürekli devam etmesi ve d ye basılırsa döngüden çıkıp görüntülemeyi bırakması için

yanlış olan
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
      break
capture.release()
cv.destroyAllWindows()
bu şekilde yazılınca videokaresi bitince çıkar 
doğrusu şöyle

while True:
    isTrue, frame = capture.read()
  
    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
