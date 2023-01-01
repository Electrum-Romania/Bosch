from django.http import HttpResponse
from django.template import loader
from myapp.models import EdgeDetection
from django.views.decorators.csrf import csrf_exempt

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
    print(request.POST['id'])
    print(request.POST['value'])
    edge.save()
    return HttpResponse(request.POST['id'])

@csrf_exempt
def camera(request):
    print(getattr(edge, 'pos1'))
    return HttpResponse("../static/b.jpeg")

@csrf_exempt
def updateImage(request):
    
    return HttpResponse("Image updated")