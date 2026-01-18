from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.
#Genre model
class Genre(models.Model):
    genre_name = models.CharField(max_length=50, blank=False, null=False)
    
    def __str__(self):
        return f"Genre name: {self.genre_name}"
    
#Movie Model    
class Movie(models.Model):
    #Rating choices
    RATING_CHOICES = [
        ('APT', 'Apta para todo público'),
        ('7+', 'Mayores de 7 años'),
        ('12+', 'Mayores de 12 años'),
        ('15+', 'Mayores de 15 años'),
        ('18+', 'Mayores de 18 años')
    ]
    
    movie_name = models.CharField(max_length=100, blank=False, null=False)
    length_minutes = models.IntegerField(blank=False, null=False)
    synopsis = models.TextField(blank=False, null=False)
    release_date = models.DateField(blank=False, null=False)
    rating = models.CharField(max_length=4, choices=RATING_CHOICES, blank=False, null=False)
    is_active = models.BooleanField(default=True)
    movie_poster = models.ImageField(upload_to='images/', storage=S3Boto3Storage)
    
    def __str__(self):
        return f"Movie name: {self.movie_name}"
   
#Classifies model    
class Classifies(models.Model):
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='classifications')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='classifications')
    
    def __str__(self):
        return f"Movie name: {self.movie_id.movie_name} Genre name: {self.genre_id.genre_name}"
    
#City model    
class City(models.Model):
    city_name = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return f"City name: {self.city_name}"
    
#Cinema model
class Cinema(models.Model):
    cinema_name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    total_seats = models.IntegerField(blank=False, null=False)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cinemas')
    
    def __str__(self):
        return f"Cinema name: {self.cinema_name} City name: {self.city_id.city_name}"

#movie show model
class MovieShow(models.Model):
    show_date = models.DateTimeField(blank=False, null=False)
    available_seats = models.IntegerField(blank=False, null=False)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_shows')
    cinema_id = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='movie_shows')
    
    def __str__(self):
        return f"Movie name: {self.movie_id.movie_name} cinema name: {self.cinema_id.cinema_name}"
    
