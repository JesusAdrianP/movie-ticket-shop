from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import *

# Create your views here.

class MovieListView(generics.ListAPIView):
    """
    View to list all movies
    GET: returns a list of all movies with their information
    Requires JWT authentication via Bearer token
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.AllowAny]

