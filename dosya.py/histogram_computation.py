import matplotlib.pyplot as plt

# Birinci renk kanalının histogramını hesapla (mavi)
hist_blue = cv.calcHist([img], [0], mask, [256], [0, 256])

# İkinci renk kanalının histogramını hesapla (yeşil)
hist_green = cv.calcHist([img], [1], mask, [256], [0, 256])

# Üçüncü renk kanalının histogramını hesapla (kırmızı)
hist_red = cv.calcHist([img], [2], mask, [256], [0, 256])

# Grafiği oluştur
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

# Her renk kanalının histogramını grafiğe ekle
plt.plot(hist_blue, color='b', label='Blue')
plt.plot(hist_green, color='g', label='Green')
plt.plot(hist_red, color='r', label='Red')

plt.legend()  # Renk kanallarını belirten legend ekleyin
plt.xlim([0, 256])  # X ekseni sınırlarını belirle

plt.show()  # Grafiği göster
