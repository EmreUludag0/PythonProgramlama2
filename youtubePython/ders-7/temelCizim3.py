import cv2

resim = cv2.imread("./resim.jpg")
#değişken ismi, başlangıç noktası, bitiş noktası, renk, kalınlık
cv2.rectangle(resim,(50,50),(150,150),(255,0,0),5)

cv2.imshow("dikdörtgen",resim)
cv2.waitKey(0)

