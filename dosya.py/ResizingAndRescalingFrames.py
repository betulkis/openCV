Çerçeveleri Yeniden Boyutlandırma ve Yeniden Ölçeklendirme

def rescaleFrame(frame, scale=0.75):
    # Images, Videos and Live Video
  
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
----
def rescaleFrame(frame, scale=0.75):
    # Fonksiyonun giriş parametreleri:
    # frame: Yeniden boyutlandırılacak görüntü çerçevesi 
    # scale: Yeniden boyutlandırma ölçeği ! (varsayılan değeri 0.75)

    # Görüntü çerçevesinin genişliğini ve yüksekliğini ölçek ! faktörüne göre hesapla
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
  
    #frame.shape[1] ifadesi, görüntünün genişliğini, frame.shape[0] ifadesi ise yüksekliğini verir.
    #scale değişkeni, kullanıcının belirlediği ölçek faktörünü ifade eder. Ölçek faktörü, mevcut genişlik ve yükseklik değerlerini çarparak veya bölerek yeni genişlik ve yükseklik değerlerini belirler.

width değişkeni, orijinal görüntü çerçevesinin genişliğini scale faktörü ile çarparak hesaplanan yeni genişliği temsil eder.

height değişkeni, orijinal görüntü çerçevesinin yüksekliğini scale faktörü ile çarparak hesaplanan yeni yüksekliği temsil eder.
    # Yeni boyutları bir tuple içinde sakla
  
    dimensions = (width, height)

    # Yeni boyutlara sahip bir görüntü çerçevesi oluştur ve döndür
  
    rescaled_frame = cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)
    
    return rescaled_frame


def changeRes(width,height):
    # Live video
  
    capture.set(3,width)
    capture.set(4,height)
----

#width ve height parametreleri, kullanıcının belirlediği yeni genişlik ve yükseklik değerleridir.

#capture.set() metodu, OpenCV kütüphanesinde bir video akışı üzerinde değişiklik yapmak için kullanılır.

#capture.set(3, width) ifadesi, video genişliğini belirtilen width değeriyle değiştirir.

#capture.set(4, height) ifadesi, video yüksekliğini belirtilen height değeriyle değiştirir
