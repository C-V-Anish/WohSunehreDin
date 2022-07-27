import imp
from django.shortcuts import render
from django.http import HttpResponse
from imdb import Cinemagoer

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
        txt=request.POST.get('SEARCHBAR','a')
        movie = ab.search_movie(txt)
        for i in range(1,10):
            print(movie[i])
    return render(request,"searchResult.html")