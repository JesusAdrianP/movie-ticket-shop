from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter, MovieShowFilter

# Create your views here.

class MovieListView(generics.ListAPIView):
    """
    View to list all movies
    GET: returns a list of all movies with their information
    Doesn't require JWT authentication
    """
    queryset = Movie.objects.prefetch_related('genres').filter(is_active = True)
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieFilter
    
class RetrieveMovieInfoView(generics.RetrieveAPIView):
    """
    View to retrieve info of specific movie
    GET: Retuns a Json with movie info
    Doesn't require JWT authentication
    """
    queryset = Movie.objects.prefetch_related('genres')
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

class ListMovieShowsView(generics.ListAPIView):
    """
    View to list all movie shows from a movie
    GET: Returns a list of all movieshows of a specific movie
    """
    serializer_class = MovieShowSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = MovieShowFilter
    
    def get_queryset(self):
        movie_id = self.kwargs['movie_id']
        queryset = MovieShow.objects.filter(movie_id=movie_id).select_related('room')
        
        return queryset

class RetrieveMovieshowView(generics.RetrieveAPIView):
    """
    View lo retrieve info about a movie show
    GET: Returns a Json with movie show info
    """
    queryset = MovieShow.objects.all()
    serializer_class = MovieShowSerializer
    permission_classes = [permissions.AllowAny]
    
class ListCitiesView(generics.ListAPIView):
    """
    View to list all registered cities
    GET: Retuns a list of json with cities names and ids
    Doesn't require JWT authentication
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]