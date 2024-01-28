import pytesseract as pyt
import cv2

kamera = cv2.VideoCapture(0)

while True:
    roi, frame = kamera.read()
    yazi = pyt.image_to_string(frame)

    with open("./proje-00/kameraNotlari.txt", "a", encoding="utf-8") as dosya: 
        dosya.writelines(yazi)
        
    print(yazi)

