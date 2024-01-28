import pygame
from tkinter import messagebox 
from random import randint as rnd #rastgele tam sayı 

pygame.init() # pygame modülünü başlatır.

genislik, yukseklik = 800, 600
HIZ = 10 # karakterin hızını belirleme
FPS = 30
sayac = 0
karakterBoyut = (50,50)
CAN = 100
TIMER = pygame.time.Clock() #fps hız özelliği ile birlikte kullanacağım.


######################################################################################### 
x_konumu = rnd(80,700)
y_konumu = rnd(80,500)

x_konumu2 = rnd(80,700)
y_konumu2 = rnd(80,500)

#pygame pencere boyutunu ayarla
pencere = pygame.display.set_mode((genislik,yukseklik)) #siyah ekran oluşturur. tek parantez kabul etmiyor

#karakter işlemleri
karakter = pygame.image.load("./mario32px.png") #fotoğrafı pygame'e yükler
karakter_bilgi = karakter.get_rect() #karakterin sinirlarini çizdiriyoruz
karakter_bilgi.topleft=(328,231) #karakterin ekrandaki konumu
karakter2 = karakter.get_size()

#bunu ben yaptım, ekstra olarak düzenlenecek
karakterYeme = pygame.image.load("./marioYeme1.png")
karakterYemeBilgi = karakter.get_rect()

worm = pygame.image.load("./solucan20px.png")
worm_bilgi = worm.get_rect()
worm_bilgi.topleft = (x_konumu2+10,y_konumu2+10)

elma = pygame.image.load("./elma.png")
elma_bilgi = elma.get_rect() 
elma_bilgi.topleft = (x_konumu,y_konumu) #elmanın ekrandaki konumunu rastgele belirler

#########################################################################################

#arka plan ses ekleme fonksiyonu
def ZEMIN_SES():
    pygame.mixer_music.load("./oyun_arka_plan.wav")
    pygame.mixer_music.play(-1,0.0)

def YEME_SESI():
    pygame.mixer_music.load("./zipla.wav")
    pygame.mixer_music.play(-1,0.0)

#SES = pygame.mixer.Sound("./zipla.wav") # mouse ile tıklandığında ses verir
#SES2 = pygame.mixer.Sound("./loss.wav")


ZEMIN_SES()
kontrol = True #sürekli döngü olmasını sağlayan sigorta
while kontrol:
    print(karakter_bilgi)
    pencere.fill((210,214,222)) #pencere iç rengi (rgb)

    for olay in pygame.event.get(): #kullanıcıdan gelen tüm olayları sürekli olarak kontrol eder ve bu olaylara göre uygulamayı günceller.
        if(olay.type == pygame.QUIT): #kapatma düğmesini tıklanıp tıklamadığını kontrol eder
            evet= messagebox.askyesno("EXIT","Emin misiniz?")
            if evet:
                kontrol = False
            else:
                kontrol=True

        # mouse ile tıklama olaylarının yapıldığı kısım (ekranda tıklama)
        if(olay.type == pygame.MOUSEBUTTONDOWN):
            #print(olay) # olay.pos > (x,y) değerlerini bir değişkene atar
            Mouse_x = olay.pos[0] # mouse x koordinatı
            Mouse_y = olay.pos[1] # mouse y koordinatı
            pencere.fill((210,214,222))
            
            #pygame.time.delay(500) #tıklanan alanın daha geç algılanmasını sağlar.
            
            #karakterin bulunduğu konumunu güncelleme
            karakter_bilgi.x = Mouse_x 
            karakter_bilgi.y = Mouse_y
            #SES.play()

    kenarlar =   pygame.draw.rect(pencere, (0,0,0,0),(50,50,700,500),width=3)
    # kenarlar =   pygame.draw.rect(neredeOlusacagi, renk, (x,y, w,h))

    #tuş basılı tutulduğındaki olaylar
    basilanTus =  pygame.key.get_pressed() #basılı tuttuğu tuşun kodunu hafızada tut
    if(basilanTus[pygame.K_d]):
        karakter_bilgi.x += HIZ
    elif (basilanTus[pygame.K_a]):
        karakter_bilgi.x -= HIZ
    elif (basilanTus[pygame.K_w]):
        karakter_bilgi.y -= HIZ
    elif (basilanTus[pygame.K_s]):
        karakter_bilgi.y += HIZ

    #karakter çerçeveye çarptığında ekranın ortasına getirir
    if(karakter_bilgi[0]<50 or karakter_bilgi[0]>700) or \
        (karakter_bilgi[1]<50 or karakter_bilgi[1] >500):
         karakter_bilgi.topleft=(328,231)

    # solucan ile mario çarpışma aşaması
    if(karakter_bilgi.colliderect(worm_bilgi)):
        #mario can yazısı eklenecek
        worm_bilgi.x = rnd(80,700)
        worm_bilgi.y = rnd(80,700)

        CAN -= 5

    # elma ile marip çarpışma aşamsı ve büyüme aşaması
    if(karakter_bilgi.colliderect(elma_bilgi)):
        pencere.blit(karakterYeme,karakterYemeBilgi)        
        elma_bilgi.x = rnd(80,700)
        elma_bilgi.y = rnd(80,500)
        sayac += 1
        if sayac == 2: #karakterin büyüme kısmı buradadır
            #sayac = 0
            karakter = pygame.transform.scale(karakter, (int(karakterBoyut[0]+10),
                                                        int(karakterBoyut[1]+10)))
            pencere.blit(karakter,[400,300])
        elif sayac == 20:
            from tkinter import messagebox
            messagebox.showwarning("yemek zamani", "yeterince yemek yenildi")
            karakter = pygame.transform.scale(karakter, karakterBoyut)
            karakterBoyut = karakter.get_size()
            sayac = 0

    #elma yediğinde karakter değişecek (deneysel)
    #if(karakter_bilgi.colliderect(elma_bilgi)):            
            

    
    myFont= pygame.font.SysFont("consolas", 12) #sistem fontunu verir
    canYazi= myFont.render(f"CAN: {str(CAN)}", True, (0,0,0))
    yazi = myFont.render("FPS: "+str(FPS),True,(0,0,0)) #fps kısmını özelleştirme
    yazi2 = myFont.render("SAYAC: "+str(sayac),True,(0,0,0)) #elma yeme sayacı
    
    for adim in range(worm_bilgi.x, 80):
        worm_bilgi.x -= HIZ

    pencere.blit(canYazi,(70,20)) #ekrana yazdırma ve konum
    pencere.blit(yazi, (600,20)) #ekrana yazdırma ve konum
    pencere.blit(yazi2, (500,20)) #ekrana yazdırma ve konum

    pencere.blit(worm,worm_bilgi)
    pencere.blit(elma,elma_bilgi) #elmayı ekranda gösterir
    pencere.blit(karakter,karakter_bilgi) #karakteri ekranda gösterir

    pygame.display.update() # güncellenip güncellemediğini kontrol eder.
    TIMER.tick(FPS)
    
pygame.quit() # pygame modülünü bitirir