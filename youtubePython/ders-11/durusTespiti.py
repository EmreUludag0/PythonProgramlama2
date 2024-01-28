import cv2
import mediapipe as mp

video = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose
mp_cizim = mp.solutions.drawing_utils

with mp_pose.Pose(static_image_mode=False,min_detection_confidence=0.5, min_tracking_confidence= 0.5) as  pose:
    while True:
        kontrol, cerceve = video.read()
        if kontrol == False:
            break
        rgb = cv2.cvtColor(cerceve,cv2.COLOR_BGR2RGB)
        sonuc = pose.process(rgb)
        #hat tespiti, çizim yapılması için gerekli olan listedir. 
        if sonuc.pose_landmarks:
            mp_cizim.draw_landmarks(cerceve,sonuc.pose_landmarks,mp_pose.POSE_CONNECTIONS) # mp_cizim.DrawingSpec((255,0,0),1,7), mp_cizim.DrawingSpec((0,3,255),2)
        cv2.imshow("durus tespiti",cerceve)
         
        if cv2.waitKey(10) == 27:
            break

video.release()
cv2.destroyAllWindows()

 