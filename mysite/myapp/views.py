from django.http import HttpResponse
from django.template import loader
# Create your views here.


def index(request):
    template = loader.get_template('index.html')
    context = {
        'image': 'rat-car-9553952.png',
    }

    return HttpResponse(template.render(context, request))
