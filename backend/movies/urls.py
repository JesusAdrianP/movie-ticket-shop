from django.urls import path
from .views import *

urlpatterns = [
    path('list_movies', MovieListView.as_view(), name='List-movies'),
    path('movie/<int:pk>', RetrieveMovieInfoView.as_view(), name='Retrieve-movie'),
    path('movie_shows/movie/<int:movie_id>', ListMovieShowsView.as_view(), name='List-movie-shows'),
    path('list_cities', ListCitiesView.as_view(), name='List-cities'),
    path('movie_show/<int:pk>', RetrieveMovieshowView.as_view(), name='Retrieve-movie-show')
]