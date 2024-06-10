import cv2
from cvzone.HandTrackingModule import HandDetector # cvzone usa o mediapipe

webcam = cv2.VideoCapture(0)
tracker = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    sucesso, imagem = webcam.read()
    coordinates, hands_image = tracker.findHands(imagem)

    cv2.imshow("IA - Activate", imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()