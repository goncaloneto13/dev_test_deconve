
from django.http import StreamingHttpResponse
from django.http import HttpResponse

from .models import *
from django.shortcuts import render
from rest_framework import viewsets
from .models import Video
from .serializers import VideoSerializer
import cv2
import threading
from django.views.decorators import gzip
import mediapipe as mp


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

@gzip.gzip_page
def Home(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        pass
    return render(request, 'app1.html')

#to capture video class
class VideoCamera(object):
    def __init__(self):

        self.s_recognizer = mp.solutions.face_detection
        self.face_recognizer = self.s_recognizer.FaceDetection()
        self.draw = mp.solutions.drawing_utils

        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

            lista_rostos = self.face_recognizer.process(self.frame)

            if lista_rostos.detections:
                for rosto in lista_rostos.detections:
                    self.draw.draw_detection(self.frame, rosto)

            key = cv2.waitKey(5)
            if key == ord('p'):
                break
            if key == ord('q'):
                cv2.waitKey(-1)        


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')       





# Create your views here.
