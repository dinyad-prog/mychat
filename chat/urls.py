
from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
path('chat/', views.index, name='index'),
path('fen/', views.index, name='fen'),
path('chat/<str:room_name>/<str:user_name>/', views.room, name='room'),

]