#çizgiden geçen arabaların sayısını veren program
import cv2

video = cv2.VideoCapture("./traffic.avi")
bg = cv2.createBackgroundSubtractorMOG2() #zemin ile hareketli nesneleri birbirinden ayırmak için kullanılır.
sayac = 0 #araç sayısı başlangıçta sıfır olsun.

while True:
    roi, frame = video.read() #roi= videodaki hareketli nesneler için kullanılan değerdir.
    if roi:
        bgCikar = bg.apply(frame) #frame görselinde arka planı çıkar
        #iki çizgiyi görsele ekleme
        cv2.line(frame, (50,0), (50,300),(255,255,255),2)
        cv2.line(frame, (70,0), (70,300),(255,255,255),2)

        #nesnelerin koordinatlarını daha hassas bulmak için kullanılır.
        #cv2.findContours() > RETR_TREE ve CHAIN_APPROX_SIMPLE
        konturler, hiyerarsi = cv2.findContours(bgCikar, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        #çıkacak olan hataları engellemek için kullanılır.
        try: hiyerarsi =hiyerarsi[1]
        except: hiyerarsi = []

        for kontur, hiy in zip(konturler, hiyerarsi):
            (x,y, w,h) = cv2.boundingRect(kontur) #kontur içerisinden çekmesi için kullanılır.
            #araçların boyutlarını giriyoruz
            if(w>10 and h>40):
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0),1)
                if(x > 50 and x<70):
                    sayac +=1

        #video üzerine yazılar yazacağız
        cv2.putText(frame,"arac "+ str(sayac), (150,150), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(255,255,255,),1)

        cv2.imshow("arac sayisi", frame) #ekranda gösterir

        if (cv2.waitKey(1) & 0xFF == ord("x")):
            cv2.destroyAllWindows()
            break

