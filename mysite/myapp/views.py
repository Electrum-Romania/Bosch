from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
from myapp.models import EdgeDetection
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import gzip

from PIL import Image
import base64
import cv2
import threading

# Create your views here.
edge, created = EdgeDetection.objects.get_or_create(name='edges')

def index(request):
    template = loader.get_template('index.html')
    
    context = {
        'maxVal': getattr(edge, 'maxVal'),
        'minVal': getattr(edge, 'minVal'),
        'pos1': getattr(edge, 'pos1'),
        'pos2': getattr(edge, 'pos2'),
        'pos3': getattr(edge, 'pos3'),
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def load(request):
    setattr(edge, request.POST['id'], request.POST['value'])
    edge.save()
    return HttpResponse(request.POST['id'])

@csrf_exempt
def camera(request):
    return HttpResponse("../static/frame.jpg")

@csrf_exempt
def updateImage(request):

    image = request.body
    
    frame = open('myapp/static/frame.jpg', 'wb')
    frame.write(image)
    frame.close()

    return HttpResponse("Image updated")

class VideoCamera(object):
    def __init__(self):
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


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def videoFeed(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass