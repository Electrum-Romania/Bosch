from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
from myapp.models import EdgeDetection
from django.views.decorators.csrf import csrf_exempt

from PIL import Image
import base64

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

    image = request.body;
    
    frame = open('myapp/static/frame.jpg', 'wb');
    frame.write(image);
    frame.close();

    return HttpResponse("Image updated")


def gen(camera):
    

	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
				b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def webcam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),
					content_type='multipart/x-mixed-replace; boundary=frame')
