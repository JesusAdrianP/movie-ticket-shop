from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

# Create your models here.
#Genre model
class Genre(models.Model):
    """
    Genre for a movie: Terror, Acción, etc
    """
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
    genres = models.ManyToManyField(Genre, through='Classifies', related_name='movies', help_text="Genres to which the movie belongs")
    
    def __str__(self):
        return f"Movie name: {self.movie_name}"
   
#Classifies model    
class Classifies(models.Model):
    """
    Movie and Genre many to many, for movies classified on most than one genre, ej:  
    Los vengadores: Acción, Ciencia ficción
    """
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='classifications_movie')
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='classifications_genre')
    
    def __str__(self):
        return f"Movie name: {self.movie_id.movie_name} Genre name: {self.genre_id.genre_name}"
    
#City model    
class City(models.Model):
    city_name = models.CharField(max_length=100, blank=False, null=False)
    
    def __str__(self):
        return f"City name: {self.city_name}"
    
#Cinema model
class Cinema(models.Model):
    """
    Cinema ej: CineColombia-Chipichape - Calle 38 Norte # 6N-45 - Cali - 30 sillas totales
    """
    cinema_name = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    total_seats = models.IntegerField(blank=False, null=False)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE, related_name='cinemas')
    
    def __str__(self):
        return f"Cinema name: {self.cinema_name} City name: {self.city_id.city_name}"

class CinemaRoom(models.Model):
    """
    Room cinema model ej: CineColombia-Chipichape - Sala 3 - Filas: [A,B,C] 
    - 10 sillas por fila -> A1,A2,..., A10, B1,...,B10 
    """
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE, related_name='cinema')
    room_name = models.CharField(max_length=50, blank=False, null=False)
    rows = models.JSONField()
    seats_per_row = models.PositiveBigIntegerField()
    
    def __str__(self):
        return f"{self.room_name} - {self.cinema.cinema_name}"

#movie show model
class MovieShow(models.Model):
    """
    Movie show ej: Avatar - 20-01-2026 h:20:00 - CineColombia-Chipichape - 20 sillas disponibles 
    """
    show_date = models.DateTimeField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2,blank=False, null=False, default=0)
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='movie_shows')
    room = models.ForeignKey(CinemaRoom, on_delete=models.CASCADE, related_name='rooms', default=None)
    
    def __str__(self):
        return f"Movie name: {self.movie_id.movie_name} - cinema name: {self.room.cinema.cinema_name}"
    
