from django.shortcuts import render
from django.http import HttpResponse

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
    return HttpResponse("WatchList Page")

def recommendations(request):
    return HttpResponse("Recommendations Page")