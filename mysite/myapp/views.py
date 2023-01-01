from django.http import HttpResponse
from django.template import loader
from myapp.models import EdgeDetection
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    edge = EdgeDetection()
    context = {
        'image': 'rat-car-9553952.png',
        'maxVal': edge.getMaxVal,
    }

    

    return HttpResponse(template.render(context, request))

def load(request):
    return HttpResponse(EdgeDetection.getMaxVal)
