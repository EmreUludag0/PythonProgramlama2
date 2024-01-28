import cv2
import numpy as np

Foto = cv2.imread("./Foto4.jpg")

FotoEn = Foto.shape[1] #görüntünün genişliğini (sütun sayısı) alır 
FotoBoy = Foto.shape[0] #görüntünün yüksekliğini (satır sayısı) alır
FotoBlob = cv2.dnn.blobFromImage(Foto, 1/256, (416,416), swapRB= True, crop=False)
#bilgisayarın anlayacağı Fotoğraf formatına çevirir

labels = ["person","bicycle","car","motorcycle","airplane","bus","train","truck","boat",
          "trafficlight","firehydrant","stopsign","parkingmeter","bench","bird","cat",
          "dog","horse","sheep","cow","elephant","bear","zebra","giraffe","backpack",
          "umbrella","handbag","tie","suitcase","frisbee","skis","snowboard","sportsball",
          "kite","baseballbat","baseballglove","skateboard","surfboard","tennisracket",
          "bottle","wineglass","cup","fork","knife","spoon","bowl","banana","apple",
          "sandwich","orange","broccoli","carrot","hotdog","pizza","donut","cake","chair",
          "sofa","pottedplant","bed","diningtable","toilet","tvmonitor","laptop","mouse",
          "remote","keyboard","cellphone","microwave","oven","toaster","sink","refrigerator",
          "book","clock","vase","scissors","teddybear","hairdrier","toothbrush"]

renkler = ["0,255,255", "176,224,230", "138,43,226", "250,235,215", "220,20,60", "154,205,50"]

#renkler dizisindeki her bir değeri virgülden böl ve int türüne atamasını yap
renkler = [ np.array(renk.split(",")).astype("int") for renk in renkler] #tek satırda for döngüsüdür

renkler = np.array(renkler)
renkler = np.tile(renkler, (15,1))

model = cv2.dnn.readNetFromDarknet("./yolov3.cfg","./yolov3.weights") #öğrenme ağlarını çağıran koddur.
layers = model.getLayerNames() #models içindeki yolo adına sahip etiketleri bul
outPutLayers = [layers[layer-1] for layer in model.getUnconnectedOutLayers()]

print(outPutLayers)

model.setInput(FotoBlob)  # Fotoğrafı model ile eşleştir
bulunanKatmanlar = model.forward(outPutLayers)

idlist = []
dortgenList = []
guvenirliklist = []

for katmanlar in bulunanKatmanlar:
    for nesne in katmanlar:
        puanlar = nesne[5:]
        tahminiID = np.argmax(puanlar)
        guvenpuani = puanlar[tahminiID]
        
        # bulmuş olduğu etiket %50 üzerinde ise oraya tahmin ettiği nesneyi çizdir
        if(guvenpuani > 0.50):    
            etiket = labels[tahminiID]
            dortgen = nesne[0:4] * np.array([FotoEn, FotoBoy,FotoEn, FotoBoy])
            (dortgen_merkez_X, dortgen_merkez_Y, dortgenEN, dortgenBOY) = dortgen.astype("int")
            
            startX = int(dortgen_merkez_X - (dortgenEN / 2))
            startY = int(dortgen_merkez_Y - (dortgenBOY / 2))
            
            # bulduğu değerleri id listesi içine ekle
            idlist.append(tahminiID)
            guvenirliklist.append(float(guvenpuani))  # çok fazla ondalık gelmesini istemiyoruz
            dortgenList.append([startX, startY, int(dortgenBOY), int(dortgenEN)]) # dortgende tam degerleri alsın

maxGuvenirlikID = cv2.dnn.NMSBoxes(dortgenList, guvenirliklist, 0.5, 0.4)

for maxID in maxGuvenirlikID:
    nesneID = maxID
    kutu = dortgenList[nesneID]
    
    # dortgen çizdirme işlemine başlıyoruz
    startX = kutu[0]
    startY = kutu[1]
    dortgenEN = kutu[2]
    dortgenBOY = kutu[3]
    
    tahminiID = idlist[nesneID]
    etiket = labels[tahminiID]
    guvenpuani2 = guvenirliklist[nesneID]
            
    endX = startX + dortgenEN
    endY = startY + dortgenBOY  
    
    dortgenRengi = renkler[tahminiID]
    dortgenRengi = [ int(renkKodu) for renkKodu in dortgenRengi ]
    
    # bulduğu nesnenin yüzdelik dilimini bize çıktı olarak göster
    yuzde = "{} - {:.2f}".format(etiket, guvenpuani2 * 100)
    
    cv2.rectangle(Foto, (startX, startY), (endX, endY), dortgenRengi, 1)
    cv2.putText(Foto, yuzde, (startX, startY-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, dortgenRengi, 2)


cv2.imshow("Fotograf yolu", Foto)
cv2.waitKey(0)



