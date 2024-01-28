import pytesseract as pyt
import PIL, cv2

foto = PIL.Image.open("./text2.jpg")
yazi = pyt.image_to_string(foto)

print(yazi)

with open("./notlar.txt", "w",encoding="utf-8") as dosya:
    dosya.writelines(yazi)

