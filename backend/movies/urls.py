from django.urls import path
from .views import *

urlpatterns = [
    path('list_movies', MovieListView.as_view(), name='List-movies')
]