import cv2

video = cv2.VideoCapture("catVideo.mp4")

while True:
    kontrol, videoMatris = video.read()

    cv2.imshow("video",videoMatris)
    if cv2.waitKey(10) == 27:
        break