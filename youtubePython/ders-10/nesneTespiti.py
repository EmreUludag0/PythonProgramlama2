import cv2
import mediapipe as mp

#nesne tanıma modülüdür, resimlerde ve videolarda nesneleri algılamak için kullanılır
mp3d = mp.solutions.objectron
# 3 boyutlu çizim işlemleri için ve landmark kullanımı için eklenir.
mp3dCizim = mp.solutions.drawing_utils


resim = cv2.imread("./ayakkabi.jpg")
resim = cv2.resize(resim, (500,500)) #yeniden boyutlandırır.


#/  static_image_mode,  görüntüde hareket yok bu yüzden true girilir. Video veya webcam için False kullanılır
#/  max_num_objects, görüntüde tespit edilecek max nesne sayısıdır.
#/  min_detection_confidence, bir nesnenin tespit edilme olasılığıdır.
#/  min_tracking_confidence, bir nesnein izlenmesi olasılığının min değeridir. yani konum bulur.
#/  model_name, nesne tanıma için kullanılacak model ismidir. 
with mp3d.Objectron(static_image_mode = True, max_num_objects=1, min_detection_confidence=0.3, min_tracking_confidence=0.3,model_name="Shoe") as nesne_3d:
    rgb = cv2.cvtColor(resim,cv2.COLOR_BGR2RGB) #görüntüyü rgb formatına dönüştürür
    sonuc = nesne_3d.process(rgb)
    if sonuc.detected_objects: #nesnelerin tespit edilip edilmediğini kontrol eder.
        for tespit in sonuc.detected_objects: # görüntüde tespit edilen her nesneyi işler.

            #  resim, nesnenin çizileceği yer,
            #  tespit.landmarks_2d, nesnenin 2d izdüşümlerini içeren bir dizi
            #  mp3d.BOX_CONNECTIONS, nesnenin 2d izdüşümlerinin nasıl çizileceğini belirleyen bir dizi
            #  mp3dCizim.DrawingSpec((255,0,0),10,5), bu dizi, rengini, kalınlığını ve çizgi stilini belirtir.
            #  mp3dCizim.DrawingSpec((0,0,255),2), nesnenin 2d izdüşümlerinin çizileceği renk ve kalınlık özellikler, verir
            mp3dCizim.draw_landmarks(resim,tespit.landmarks_2d, mp3d.BOX_CONNECTIONS,mp3dCizim.DrawingSpec((255,0,0),10,5),mp3dCizim.DrawingSpec((0,0,255),2))
        cv2.imshow("3d", resim)
        cv2.waitKey(0)   



        