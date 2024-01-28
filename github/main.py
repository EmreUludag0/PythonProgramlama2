import cv2, numpy as np
from collections import deque  # Listeler oluşturmak için kullanacağız

camera = cv2.VideoCapture(0)

# çizim işlemlerinde kullanacağımız maskeleme için tanımlamalar yapıyoruz
lowerBlue = np.array([100,60,60])
upperBlue = np.array([140,255,255])

# renk listelerini saklıyoruz
kirmiziNoktalar = [deque(maxlen=512)]
sariNoktalar = [deque(maxlen=512)]
maviNoktalar = [deque(maxlen=512)]
yesilNoktalar = [deque(maxlen=512)]

kirmiziIndex = 0
sariIndex = 0
maviIndex = 0
yesilIndex = 0

renkler = [(0,0,255), (0,255,255), (255,0,0),(0,255,0) ]
renkIndexleri = 0

cizimPenceresi = np.ones((600,800,3))

# Düğmeleri oluşturduk ve renklendirdik
cizimPenceresi = cv2.rectangle(cizimPenceresi, (25,5), (150,50), (0,0,0), 2)
cizimPenceresi = cv2.rectangle(cizimPenceresi, (175,5), (300,50), renkler[0], -1)
cizimPenceresi = cv2.rectangle(cizimPenceresi, (325,5), (450,50), renkler[1], -1)
cizimPenceresi = cv2.rectangle(cizimPenceresi, (475,5), (600,50), renkler[2], -1)
cizimPenceresi = cv2.rectangle(cizimPenceresi, (625,5), (750,50), renkler[3], -1)

# Düğmelerin Yazılarını yazdık
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

cv2.putText(cizimPenceresi,"CLEAR ALL", (40,30),font,0.5, (0,0,0), 1, cv2.LINE_AA)
cv2.putText(cizimPenceresi,"KIRMIZI", (190,30),font,0.5, renkler[1], 1, cv2.LINE_AA)
cv2.putText(cizimPenceresi,"SARI", (350,30),font,0.5, renkler[0], 1, cv2.LINE_AA)
cv2.putText(cizimPenceresi,"MAVI", (500,30),font,0.5, (255,255,255), 1, cv2.LINE_AA)
cv2.putText(cizimPenceresi,"YESIL", (650,30),font,0.5, (255,255,255), 1, cv2.LINE_AA)


# cv2.namedWindow("Paint")  Başlık adı veriyoruz

while True:
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (800,600))
    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Düğmeleri oluşturduk ve renklendirdik
    frame = cv2.rectangle(frame, (25,5), (150,50), (0,0,0), 2)
    frame = cv2.rectangle(frame, (175,5), (300,50), renkler[0], -1)
    frame = cv2.rectangle(frame, (325,5), (450,50), renkler[1], -1)
    frame = cv2.rectangle(frame, (475,5), (600,50), renkler[2], -1)
    frame = cv2.rectangle(frame, (625,5), (750,50), renkler[3], -1)

    # Düğmelerin Yazılarını yazdık
    cv2.putText(frame,"CLEAR ALL", (40,30),font,0.5, (0,0,0), 1, cv2.LINE_AA)
    cv2.putText(frame,"KIRMIZI", (190,30),font,0.5, renkler[1], 1, cv2.LINE_AA)
    cv2.putText(frame,"SARI", (350,30),font,0.5, renkler[0], 1, cv2.LINE_AA)
    cv2.putText(frame,"MAVI", (500,30),font,0.5, (255,255,255), 1, cv2.LINE_AA)
    cv2.putText(frame,"YESIL", (650,30),font,0.5, (255,255,255), 1, cv2.LINE_AA)
    
    # programda hata varsa bitir
    if _ is False:
        break
    
    # maskeleme yapıyoruz
    maske = cv2.inRange(HSV, lowerBlue, upperBlue)
    maske = cv2.erode(maske, (5,5), iterations=1) # maskenin daha iyi olmasını sağlıyor
    maske = cv2.morphologyEx(maske, cv2.MORPH_OPEN, (5,5))
    maske = cv2.dilate(maske, (5,5), iterations=1) # seçimi kalınlaştırıyoruz
    maske = cv2.medianBlur(maske, 5) # maskeyi temizliyoruz
    
    # kontur işlemleri
    konturlar, _ = cv2.findContours(maske, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    # SİLGİ mavi nesneye çember ekliyoruz. Nesne düğmelerin üzerine gelince seçsin ve çizim yapsın
    center = None
    
    try:
        if (len(konturlar) > 0):
            maxKontur = sorted(konturlar, key=cv2.contourArea, reverse=True)[0] # elimizdeki en büyük konturu bulmak sırala ve [0] ile en baştakine eriş
            ((x,y), radius) = cv2.minEnclosingCircle(maxKontur)
            cv2.circle(frame, (int(x),int(y)), int(radius), renkler[0], 3)

            M = cv2.moments(maxKontur)
            center = (int(M["m10"]/M["m00"]),int(M["m01"]/M["m00"]))
                
            # düğmelerin olduğu yere maske geldi mi
            if (center[1] <= 50):
                if (25 < center[0] < 150):
                    kirmiziNoktalar = [deque(maxlen=512)]
                    sariNoktalar = [deque(maxlen=512)]
                    maviNoktalar = [deque(maxlen=512)]
                    yesilNoktalar = [deque(maxlen=512)]

                    kirmiziIndex = 0
                    sariIndex = 0
                    maviIndex = 0
                    yesilIndex = 0
                    
                    cizimPenceresi[60:,:,:] = 255 # ekranı düğmelerin altından beyaza boya
                elif (175 < center[0] < 300):
                    renkIndexleri = 0
                elif (325 < center[0] < 450):
                    renkIndexleri = 1
                elif (475 < center[0] < 600):
                    renkIndexleri = 2
                elif (625 < center[0] < 750):
                    renkIndexleri = 3
            else:
                if (renkIndexleri == 0):
                    kirmiziNoktalar[kirmiziIndex].appendleft(center)
                if (renkIndexleri == 1):
                    sariNoktalar[sariIndex].appendleft(center)
                if (renkIndexleri == 2):
                    maviNoktalar[maviIndex].appendleft(center)
                if (renkIndexleri == 3):
                    yesilNoktalar[yesilIndex].appendleft(center)
        else:
            # indexleri artırıyoruz
            kirmiziNoktalar.append(deque(maxlen=512))
            kirmiziIndex +=1
            
            sariNoktalar.append(deque(maxlen=512))
            sariIndex +=1
            
            maviNoktalar.append(deque(maxlen=512))
            maviIndex +=1
            
            yesilNoktalar.append(deque(maxlen=512))
            yesilIndex +=1
    except Exception as hata:
        print("Hata Kodu.:", hata)
                
    renkListesi = [kirmiziNoktalar, sariNoktalar, maviNoktalar, yesilNoktalar]
    
    for renk in range(len(renkListesi)):
        for r in range(len(renkListesi[renk])):
            for k in range(len(renkListesi[renk][r])):
                if (renkListesi[renk][r][k -1] is None) or (renkListesi[renk][r][k] is None):
                    continue
                cv2.line(frame, renkListesi[renk][r][k -1], renkListesi[renk][r][k], renkler[renk], 3)
                cv2.line(cizimPenceresi, renkListesi[renk][r][k -1], renkListesi[renk][r][k], renkler[renk], 3)
                
        
                
    cv2.imshow("Ekrana Cizim", frame)
    cv2.imshow("WebCam Paint", cizimPenceresi)
    if (cv2.waitKey(5) == 27):
        break


cv2.destroyAllWindows()

