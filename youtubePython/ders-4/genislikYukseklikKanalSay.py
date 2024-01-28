import cv2

res = cv2.imread("./resim.jpg")
yukseklik, genislik, kanalSayisi = res.shape
print("yukseklik: {} Genislik: {} Kanal Sayisi: {}".format(yukseklik,genislik,kanalSayisi))