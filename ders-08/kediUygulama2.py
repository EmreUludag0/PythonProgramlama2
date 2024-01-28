import cv2

kedi = cv2.VideoCapture("./kedi.mp4")
kediCascade = cv2.CascadeClassifier("./cat.xml")

while True:
    try:
        roi, frame = kedi.read()
        gri = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kedi2 = kediCascade.detectMultiScale(gri, 1.2,2)

        for(x,y,w,h) in kedi2:
            cv2.rectangle(frame, (x,y),(x+w, y+h), (0,255,0),2)

        cv2.imshow("kediler", frame)

        if(cv2.waitKey(1) % 0xFF == ord("x")):
            cv2.destroyAllWindows()
            break
    except:
        cv2.destroyAllWindows()
        break
