from django.contrib import admin
from .models import Movie, MovieShow, Cinema, City, Classifies, Genre, CinemaRoom
from .forms import CinemaRoomForm

# Register your models here.
class ClassifiesInline(admin.TabularInline):
    """
    Model custom class to add a genre to a movie in admin panel
    """
    model = Classifies
    autocomplete_fields = ['genre_id']
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """
    Genre admin custom class to display genre_id and name
    And adding name to search_field to search by name
    """
    list_display = ('id','genre_name')
    search_fields = ['name']

@admin.register(MovieShow)
class MovieShowAdmin(admin.ModelAdmin):
    """
    Custom movieShow model admin to display model attributes in admin panel table
    """
    list_display = ('id','movie_id','room','price', 'show_date')

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Custom movie model admin to display model attributes in admin panel table
    And adding the custom class to add genres to a movie
    """
    list_display = ('movie_name', 'rating', 'is_active')
    inlines = [ClassifiesInline]

@admin.register(CinemaRoom)
class CinemaRoomAdmin(admin.ModelAdmin):
    """
    Custom CinemaRoom model admin to display model attributes in admin panel table
    Adding customized form to add rows more simply
    And adding search_field to search by room_name and cinema_name
    """
    form = CinemaRoomForm
    list_display = ('room_name', 'cinema', 'seats_per_row')
    search_fields = ('room_name', 'cinema__cinema_name')

@admin.register(Cinema)
class CinemaAdmin(admin.ModelAdmin):
    """
    Custom Cienam model admin to display model attributes in admin panel table
    """
    list_display = ('cinema_name', 'address', 'city_id')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Custom City model admin to display model attributes in admin panel table
    """
    list_display = ('id', 'city_name')