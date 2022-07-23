from cv2 import namedWindow
from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name="home"),
path('movies/',views.movies,name="movies"),
path('songs/',views.songs,name="songs"),
path('aboutus/',views.aboutus,name='aboutus')
]
