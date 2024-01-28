from turtle import *
from datetime import datetime

simdi = datetime.now()
saat = simdi.hour
dakika = simdi.min

def cerceve():
    penup()
    goto((-125,275))
    pendown()
    for i in range(4):
        fd(280)
        right(90)
        fd(275)
        right(90)
    

def akrep():
    penup()
    home() # 0,0 koordinatına ekranın ortasına çıkar 
    goto((0,100))
    pendown()
    forward(-70) #saatin açısını hesapla
    forward(70)
    penup()
    

def yelkovan():
    penup()
    goto(0,125)
    pendown()
    forward(dakika * 6-90)
    forward(100)
    forward(-100)

def sayilar():
    sayac = 0
    font = ("calibri", 12, "bold")
    with open("./duvarsaati.txt", encoding="utf-8") as dosya:
        for satir in dosya.readlines():
            sayac += 1
            satir = satir.replace("\n", "") # aradaki enter tuşunu sil
            satir = satir.split(",") # x ve y koordinatlarını virgülden ayır
            x, y = int(satir[0]), int(satir[1])
            goto((x,y))
            write(sayac = font) # turtle sayfa ile ilgili koordinatlara yazdır
            write(str(sayac), font=font)


def uygulama():
    delay(1)
    cerceve()
    sayilar()
    akrep()
    yelkovan()
    pencolor("blue")
    font = ("Comic Sans MS", 60, "bold italic")
    sistemSaati = str(saat) + ":" + str(dakika)
    goto(0,100)
    pendown()
    write(sistemSaati, font=font)
    mainloop() #turtle ana fonksiyonudur. pencereyi sürekli açık tutar.


uygulama()