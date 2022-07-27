import imp
from django.shortcuts import render
from django.http import HttpResponse
from imdb import Cinemagoer
import string

ab=Cinemagoer()

# Create your views here.
def index(request):
    return render(request,"index.html")

def movies(request):
    return HttpResponse("Movies Page")

def songs(request):
    return HttpResponse("Songs Page")

def aboutus(request):
    return HttpResponse("About Page")

def watchlist(request):
    return render(request,"watchlist.html")

def recommendations(request):
    return render(request,"recommendations.html")

def searchResults(request):
    if request.method=='POST':
        temp=True
        txt=request.POST.get('SEARCHBAR','a')
        movie = ab.search_movie(txt)
        id=movie[0].movieID
        film=ab.get_movie(id)
        l=len(film['cast'])
        if l>5:
            cast={'a1':film['cast'][0],'a2':film['cast'][1],'a3':film['cast'][2],'a4':film['cast'][3],'a5':film['cast'][4],'temp':temp,'movie_name':string.capwords(txt,None)}
        else:
            temp=False
            cast={'a1':film['cast'][0],'a2':film['cast'][1],'temp':temp,'movie_name':string.capwords(txt,None)}
        return render(request,"searchResult.html",cast)