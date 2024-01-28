import cv2
import pyautogui
from time import sleep

el_cascade =    cv2.CascadeClassifier("hand.xml")
kamera = cv2.VideoCapture(0)

while True:
    roi, img = kamera.read()
    gri = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    el = el_cascade.detectMultiScale(gri,1.1,4)

    for (x,y, w,h) in el:
        cv2.rectangle(img, (x,y),(x+w, y+h),(0,0,255),3)
        cv2.putText(img, "EL", (x+w, y+h), cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
        pyautogui.press("space")

    cv2.imshow("el oyunu", img)
    if cv2.waitKey(1) & 0xff == 27:
        break

kamera.release()