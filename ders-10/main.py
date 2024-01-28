# pip install pygame  > Yüklü olması gerekli
import pygame
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

uygulama = pygame.display.set_mode(PENCERE_BOYUT)

uygulama.fill((47,79,79))

ekranKontrol = 1
while ekranKontrol:
    for e in pygame.event.get():
        if (e.type == pygame.QUIT):
            ekranKontrol = 0

    uygulama.blit(zemin, (0,20))  # zemini ekranın sol üstüne hizalayarak ekle
    pygame.display.update()  # ekranda olan bir değişikliği güncelle
    
print("Program Sonlandı")
pygame.quit()
        