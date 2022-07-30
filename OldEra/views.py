from django.shortcuts import redirect, render
from django.http import HttpResponse
from imdb import Cinemagoer
import string

ab=Cinemagoer()

# Create your views here.
def index(request):
    return render(request,"index.html")

def movies(request):
    return render(request,"movies.html")

def songs(request):
    return render(request,"songs.html")

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
        if txt.strip()=="":
            return redirect('home')
        else:
            movie = ab.search_movie(txt)
            try:
                id=movie[0].movieID
                film=ab.get_movie(id)
                a=film.get('language', None)
                list=['Hindi','Tamil']
                if ((film['year'] > 1990) or (a not in list)):
                    dict={'message':'No such movie by this name exists in the RetroEra'}
                    return render(request,'error.html',dict)
                else:
                    l=len(film['cast'])
                    if l>5:
                        cast={'a1':film['cast'][0],'a2':film['cast'][1],'a3':film['cast'][2],'a4':film['cast'][3],'a5':film['cast'][4],'temp':temp,'movie_name':string.capwords(movie[0]['title'],None)}
                    else:
                        temp=False
                        cast={'a1':film['cast'][0],'a2':film['cast'][1],'temp':temp,'movie_name':string.capwords(movie[0]['title'],None)}
                    return render(request,"searchResult.html",cast)
            except:
                dict={'message':'No such movie by this name exists'}
                return render(request,"error.html",dict)
        