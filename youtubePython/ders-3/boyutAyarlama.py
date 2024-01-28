import cv2

resim = cv2.imread("./resim.jpg")

#orijinal görüntü sonra değişiklik yapılacak boyut girilir
yeniBoyut = cv2.resize(resim,(500,500))

cv2.imshow("orijinal",resim)
cv2.imshow("Boyutlandirma", yeniBoyut)

cv2.waitKey(0)