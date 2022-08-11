import cv2 
import mediapipe as mp

webcam = cv2.VideoCapture(0)
s_recognizer = mp.solutions.face_detection
face_recognizer = s_recognizer.FaceDetection()
draw = mp.solutions.drawing_utils

while True:
    verificador, frame = webcam.read()
    if not verificador:
        break

    lista_rostos = face_recognizer.process(frame)

    if lista_rostos.detections:
        for rosto in lista_rostos.detections:
            draw.draw_detection(frame, rosto)

    cv2.imshow("Rostos", frame)

    if cv2.waitKey(5) == 27:
        break

webcam.release()
cv2.destroyAllWindows()