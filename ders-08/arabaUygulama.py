import cv2

foto = cv2.imread("./arabaDeneme.jpg")
fotoCascade = cv2.CascadeClassifier("./car.xml")

griRenk = cv2.cvtColor(foto, cv2.COLOR_BGR2GRAY)
foto2 = fotoCascade.detectMultiScale(griRenk, 1.2,1)

for(x,y, w,h) in foto2:
   cv2.rectangle(foto, (x,y),(x+y, y+h), (0,255,0),2) 

cv2.imshow("araba", foto)
cv2.waitKey(0)