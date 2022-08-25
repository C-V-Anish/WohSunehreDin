from django.urls import path
from . import views

urlpatterns = [
path('',views.index,name="home"),
path('movies/',views.movies,name="movies"),
path('songs/',views.songs,name="songs"),
path('aboutus/',views.aboutus,name='aboutus'),
path('watchlist/',views.watchlist,name='watchlist'),
path('recommendations/',views.recommendations,name='recommendations'),
path('searchResults/',views.searchResults,name="SearchResults")
]
