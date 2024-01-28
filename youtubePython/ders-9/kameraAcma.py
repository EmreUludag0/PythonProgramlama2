import cv2

webcam = cv2.VideoCapture(0)

while True:
    roi, frame = webcam.read()
    gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("video",gri)
    if cv2.waitKey(10) == 27:
        break
