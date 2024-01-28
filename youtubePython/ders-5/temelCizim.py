import cv2

resim = cv2.imread("./resim.jpg")

cv2.line(resim,(50,50),(150,250),(255,0,0),4)
cv2.imshow("cizgi", resim)
cv2.waitKey(0)