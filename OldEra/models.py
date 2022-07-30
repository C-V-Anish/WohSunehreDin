from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name=models.CharField(max_length=50,primary_key=True)
    movie_img=models.ImageField(upload_to="static/images",default="")
    
    def __str__(self):
        return self.movie_name