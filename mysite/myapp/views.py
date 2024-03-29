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
# edge = EdgeDetection(name='edges')

# RPI SOCKET SERVER

host = '0.0.0.0'
port = 2244
server_socket1 = socket.socket()
server_socket1.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket1.bind((host, port))
server_socket1.listen(0)
print('listen camera socket')

host = '0.0.0.0'
port = 2255
server_socket2 = socket.socket()
server_socket2.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket2.bind((host, port))
server_socket2.listen(0)
print('listen analysis socket')

host = '0.0.0.0'
port = 2266
server_socket3 = socket.socket()
server_socket3.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server_socket3.bind((host, port))
server_socket3.listen(0)
print('listen command socket')

connection3 = server_socket3.accept()[0]
print('connected command socket')
connection1 = server_socket1.accept()[0]
print('connected camera socket')
connection2 = server_socket2.accept()[0]
print('connected analysis socket')

def index(request):
    template = loader.get_template('index.html')
    
    context = {
        'lane_perspective_floor': getattr(edge, 'lane_perspective_floor'),
        'lane_perspective_roof': getattr(edge, 'lane_perspective_roof'),
        'lane_perspective_startfloor': getattr(edge, 'lane_perspective_startfloor'),
        'lane_perspective_stopfloor': getattr(edge, 'lane_perspective_stopfloor'),
        'lane_perspective_startroof': getattr(edge, 'lane_perspective_startroof'),
        'lane_perspective_stoproof': getattr(edge, 'lane_perspective_stoproof'),
        'lane_left_rect_x': getattr(edge, 'lane_left_rect_x'),
        'lane_left_rect_y': getattr(edge, 'lane_left_rect_y'),
        'lane_left_rect_width': getattr(edge, 'lane_left_rect_width'),
        'lane_left_rect_height': getattr(edge, 'lane_left_rect_height'),
        'lane_right_rect_x': getattr(edge, 'lane_right_rect_x'),
        'lane_right_rect_y': getattr(edge, 'lane_right_rect_y'),
        'lane_right_rect_width': getattr(edge, 'lane_right_rect_width'),
        'lane_right_rect_height': getattr(edge, 'lane_right_rect_height'),
    }
    return HttpResponse(template.render(context, request))

@csrf_exempt
def load(request):
    setattr(edge, request.POST['id'], request.POST['value'])
    edge.save()
    data = request.POST['id'] + '=' + request.POST['value'] + '\r\n'
    print(data)
    connection3.send(data.encode())
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

# pressed_key=w/a/s/d 
@csrf_exempt
def manual_control(request):
    pressed_key = request.POST["pressed_key"]
    data = "pressed_key=" + pressed_key + "\r\n"
    connection3.send(data.encode())
    return HttpResponse("")

@csrf_exempt
def request_frame(request):
    analysis = request.POST["analysis"]
    data = analysis+ "\r\n"
    connection3.send(data.encode())
    return HttpResponse("")
