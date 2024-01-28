# pip install pygame  > Yüklü olması gerekli
import pygame
from datetime import datetime

pygame.init()
try:
    GENISLIK = int(input("Genişlik Değeri: "))
    YUKSEKLIK = int(input("Yükseklik Değeri: "))
    if (GENISLIK < 250 or YUKSEKLIK < 250) or (GENISLIK > 1024 or YUKSEKLIK > 800):
        print("Hatalı Değer")
        exit()
    else:
        PENCERE_BOYUT = (GENISLIK,YUKSEKLIK)
except:
    print("Hatalı Değer")
    exit()

zemin = pygame.image.load("./zemin.jpg") # arkaplan görseli eklemek
zaman = datetime.now()
uygulama = pygame.display.set_mode(PENCERE_BOYUT)
pygame.display.set_caption(str(zaman))  # pencere başlığını değiştir

uygulama.fill((47,79,79))  # pencere iç rengini ayarlıyoruz

def ciz():
    icon = pygame.image.load("./icon.png") # icon resmini değişkene atıyoruz
    pygame.display.set_icon(icon)  # icon olarak ayarlıyoruz
    pygame.draw.line(uygulama, (45,210,252), (30,30), (100,100)) # çizgi
    pygame.draw.circle(uygulama, (0,255,0), (100,100), 30 )  # daire çizdir
    pygame.draw.rect(uygulama, (255,0,0), (100,200,100,100), border_radius=10)  # dörtgen çizdirir

def fontlar():
    # for font in pygame.font.get_fonts():
    #     print(font)  #pygame içindeki fontları görüntüle
    font = pygame.font.SysFont("consolas", 20)  # pygame içindeki fontu boyutla birlikte kullan
    yazi = font.render("Pygame Yazi Islemleri", True, (255,255,0), (255,255,255))   
    # ekranda çıkmasını istediğiniz yazıyı yazıyoruz ve 4. parametre yazıarkaplan rengi
    # yaziKoordinat = yazi.get_rect()  # yazının alanını dörtgen ile kaplıyoruz
    # yaziKoordinat.topleft = (200,100)  # ekranın 200x100 konumunda çıksın
    uygulama.blit(yazi, (200,100))
    
# programı sürekli çalıştıran döngü 
ekranKontrol = 1
while ekranKontrol:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            ekranKontrol = 0
    
    uygulama.blit(zemin, (0,20))  # zemini ekranın sol üstüne hizalayarak ekle
    ciz()
    fontlar()
    pygame.display.update()  # ekranda olan bir değişikliği güncelle
    
print("Program Sonlandı")
pygame.quit()
        