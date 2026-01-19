from django.contrib import admin
from .models import Movie, MovieShow, Cinema, City, Classifies, Genre, CinemaRoom
from .forms import CinemaRoomForm

# Register your models here.
class ClassifiesInline(admin.TabularInline):
    model = Classifies
    autocomplete_fields = ['genre_id']
    extra = 1

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(MovieShow)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    inlines = [ClassifiesInline]

@admin.register(CinemaRoom)
class CinemaRoomAdmin(admin.ModelAdmin):
    form = CinemaRoomForm
    list_display = ('room_name', 'cinema', 'seats_per_row')
    search_fields = ('room_name', 'cinema__cinema_name')

admin.site.register(Cinema)
admin.site.register(City)
admin.site.register(Classifies)