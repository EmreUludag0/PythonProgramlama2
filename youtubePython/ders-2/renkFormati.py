import cv2

#görüntü işleme yapıldığında renk formatı değiştirilmesi gerekir. makine öğrenimi için önemlidir.
resim = cv2.imread("./resim.jpg")

#üstünde değişiklik yapılacak olan resim ve sonra dönüştürülmek istenen parametre yazılır
gri = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)  
rgb = cv2.cvtColor(resim,cv2.COLOR_BGR2RGB)

cv2.imshow("gri", gri)
cv2.imshow("orijinal", resim)
cv2.imshow("rgb", rgb)
cv2.waitKey(0)