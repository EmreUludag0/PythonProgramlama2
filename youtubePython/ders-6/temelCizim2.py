import cv2

res = cv2.imread("./resim.jpg")
#değişken ismi, merkez nokta,yarı çap,renk,kalınlık
cv2.circle(res,(60,60),60,(0,255,0),3)

cv2.imshow("daire",res)
cv2.waitKey(0)