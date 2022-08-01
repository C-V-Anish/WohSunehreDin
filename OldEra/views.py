from urllib.request import urlopen
from django.shortcuts import redirect, render
from django.http import HttpResponse
from imdb import Cinemagoer, IMDbError
import string
from scraper_api import ScraperAPIClient
from bs4 import BeautifulSoup
import PIL.Image
from .models import Movie
import io

ab=Cinemagoer()
client = ScraperAPIClient("2a340d7354482b7bc8055a164dafb063")

# Create your views here.
def index(request):
    return render(request,"index.html")

def movies(request):
    if request.method=='POST':

        mov=request.POST.get('name',' ')

        if mov.strip()=="":
            return redirect('movies')
        else:

            movie = ab.search_movie(mov) 
            try:

                id=movie[0].movieID

                film=ab.get_movie(id)

                url="https://www.imdb.com/title/tt"+str(id)+"/"

                url_data=client.get(url).text

                s_data=BeautifulSoup(url_data,"html.parser")

                imdb_image=s_data.find("meta",property="og:image")

                image_link=imdb_image.attrs['content']

                u=urlopen(image_link)

                raw=u.read()

                image=PIL.Image.open(io.BytesIO(raw))

                image.save("static/images/"+str(id)+".jpg","JPEG")

                cinema=Movie(movie_name=string.capwords(movie[0]['title'],None),movie_img=image_link)

                cinema.save()

                if ((film['year'] > 1990)) :
                    dict={'message':'No such movie by this name exists in the RetroEra'}
                    return render(request,'error.html',dict)
                else:
                    dict={"image_link":image_link,"movie_name":string.capwords(movie[0]['title'],None)}
                    return render(request,'movies.html',dict)
            except (IMDbError,AttributeError) as e:
                print(e)


            
        
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

                url="https://www.imdb.com/title/tt"+str(id)+"/"

                url_data=client.get(url).text

                s_data=BeautifulSoup(url_data,"html.parser")

                imdb_image=s_data.find("meta",property="og:image")

                image_link=imdb_image.attrs['content']
                
                film=ab.get_movie(id)

                a=film.get('language', None)

                if ((film['year'] > 1990)) :
                    dict={'message':'No such movie by this name exists in the RetroEra'}
                    return render(request,'error.html',dict)
                else:
                    l=len(film['cast'])
                    if l>5:
                        cast={'a1':film['cast'][0],'a2':film['cast'][1],'a3':film['cast'][2],'a4':film['cast'][3],'a5':film['cast'][4],'temp':temp,'movie_name':string.capwords(movie[0]['title'],None),"image":image_link}
                    else:
                        temp=False
                        cast={'a1':film['cast'][0],'a2':film['cast'][1],'temp':temp,'movie_name':string.capwords(movie[0]['title'],None),"image":image_link}
                    return render(request,"searchResult.html",cast)
            except:
                dict={'message':'No such movie by this name exists'}
                return render(request,"error.html",dict)
        