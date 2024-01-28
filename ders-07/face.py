import cv2

yuzler = cv2.imread("./faces.jpg")
yuzlerCascade = cv2.CascadeClassifier("./frontalface.xml") 

gri = cv2.cvtColor(yuzler, cv2.COLOR_BGR2GRAY)
yuzler2 = yuzlerCascade.detectMultiScale(gri, 1.2, 3)

for (x,y,w,h) in yuzler2:
    cv2.rectangle(yuzler, (x,y),(x+w, y+h), (0,255,255), 2)

cv2.imshow("Yuzler", yuzler)
cv2.waitKey(0)


