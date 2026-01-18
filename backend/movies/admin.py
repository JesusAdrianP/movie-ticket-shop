from django.contrib import admin
from .models import Movie, MovieShow, Cinema, City, Classifies, Genre

# Register your models here.
admin.site.register(MovieShow)
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(City)
admin.site.register(Classifies)
admin.site.register(Genre)