from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('load/', views.load, name='load'),
    path('camera/', views.camera, name='camera'),
    path('updateImage/', views.updateImage, name='updateImage'),
]
