from django.shortcuts import render
from .serializers import CustomUserSerializer
from rest_framework import generics, permissions

# Create your views here.

#Vire to create new user
class CreateUserView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]
    