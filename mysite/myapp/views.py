from django.http import HttpResponse, StreamingHttpResponse
from django.template import loader
from myapp.models import EdgeDetection
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators import gzip

import struct
import socket
import numpy as np

# store last session parameters
edge, created = EdgeDetection.objects.get_or_create(name='edges')

# RPI SOCKET SERVER

host = '0.0.0.0'
port = 2244
server_socket1 = socket.socket()
server_socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket1.bind((host, port))
server_socket1.listen(0)
print('listen socket 1')

host = '0.0.0.0'
port = 2255
server_socket2 = socket.socket()
server_socket2.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket2.bind((host, port))
server_socket2.listen(0)
print('listen socket 2')


connection1 = server_socket1.accept()[0]
print('connected socket 1')
connection2 = server_socket2.accept()[0]
print('connected socket 2')

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
    def stream():
        while True:
            size = connection1.recv(4)
            size = int.from_bytes(size, byteorder='big')

            data = b''

            while len(data) < size:
                if len(data) + 1024 < size:
                    data += connection1.recv(1024)
                else:
                    data += connection1.recv(size - len(data))


            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + data + b'\r\n'

    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')

@csrf_exempt
def analysis(request):
    def stream():
        while True:
            size = connection2.recv(4)
            size = int.from_bytes(size, byteorder='big')

            data = b''

            while len(data) < size:
                if len(data) + 1024 < size:
                    data += connection2.recv(1024)
                else:
                    data += connection2.recv(size - len(data))


            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + data + b'\r\n'

    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')

@csrf_exempt
def manual_control(request):
    pass