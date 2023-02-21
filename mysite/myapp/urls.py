from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load', views.load, name='load'),
    path('camera', views.camera, name='camera'),
    path('analysis', views.analysis, name='analysis'),
    path('manual_control', views.manual_control, name='manual_control'),
    path('request_frame', views.request_frame, name='request_frame'),
    

    # path('updateImage', views.updateImage, name='updateImage'),
    # path('videoFeed', views.videoFeed, name='videoFeed'),
]
