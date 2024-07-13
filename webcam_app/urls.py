from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('video_feed', views.stream_video, name='video_feed'),
    path('hello', views.hello_world, name='hello_world'),
]
