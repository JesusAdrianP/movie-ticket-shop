from django_filters import rest_framework as filters
from .models import Movie

class MovieFilter(filters.FilterSet):
    """
    Advanced filter for Movies with support for JSON field filtering.

    Available filters:
    - movie_name: Partial match (case-insensitive)
    - release_date: Exact match
    - rating: Apta para todo público, Mayores de 7 años, Mayores de 12 años, Mayores de 15 años, Mayores de 18 años
    - genre: genre ID
    """
    movie_name = filters.CharFilter(lookup_expr='icontains')
    release_date = filters.DateFilter(lookup_expr='exact')
    rating = filters.ChoiceFilter(choices=Movie.RATING_CHOICES)
    genre = filters.NumberFilter(field_name='classifications_movie__genre_id', label='Genre')
    
    class Meta:
        model = Movie
        fields = [
            'movie_name', 
            'release_date',
            'rating',
            'genre'
        ]