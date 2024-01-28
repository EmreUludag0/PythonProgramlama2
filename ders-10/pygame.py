#pip install pygame > yüklü olması lazım
import pygame 
pygame.init()

try:
    
    genislik = int(input("genislik degeri: "))
    yukseklik = int(input("yukseklik degeri: "))
    pencere_boyut = (genislik, yukseklik)
    if(genislik <250 or yukseklik < 250) or (genislik > 1024 or yukseklik>800):
        print("hatali deger")
        exit()
    else:
        pencere_boyut =(genislik, yukseklik)

except:
    print("hatali deger")
    exit()
    

zemin = pygame.image.load("./zemin.jpg") #arka plana görsel eklemek

uygulama = pygame.display.set_mode(pencere_boyut) #uygulama penceresini açar

uygulama.fill((47,79,79))
uygulama.set_alpha(10)

ekranKontrol= 1
while ekranKontrol:
    for e in pygame.event.get():
        if(e.type == pygame.QUIT):
            ekranKontrol = 0
    
    uygulama.blit(zemin,(0)) #zemini ekranın sol üstüne hizalayarak ekle
    pygame.display.update() #ekranda olan bir değişikliği güncelle

            
print("program sonlandı")
pygame.quit()
        
        
        
        