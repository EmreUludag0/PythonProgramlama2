import cv2

yuzler = cv2.VideoCapture(0)
yuzlerCascade = cv2.CascadeClassifier("./frontalface.xml") 

while True:
    try:
        roi, frame = yuzler.read()
        gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        yuzler2 = yuzlerCascade.detectMultiScale(gri, 1.9, 2)

        for (x,y,w,h) in yuzler2:
            cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,255), 2)

        cv2.imshow("yuzler", frame)

        if(cv2.waitKey(1) % 0xFF == ord("x")):
            cv2.destroyAllWindows()
            break
    except:
        cv2.destroyAllWindows()
        break