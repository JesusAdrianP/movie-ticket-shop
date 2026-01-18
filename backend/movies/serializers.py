from rest_framework import serializers
from .models import City, Cinema, Classifies, Genre, Movie, MovieShow

class CitySerializer(serializers.ModelSerializer):
    """
    Serializer for City model
    used for list and create
    """
    class Meta:
        model = City
        fields = '__all__'
        read_only_fields = ['id']
        
    def create(self, validated_data):
        city = City.objects.create(**validated_data)
        city.save()
        return city
    
class CinemaSerializer(serializers.ModelSerializer):
    """
    Serializer for Cinema model
    """
    class Meta:
        model = Cinema
        fields = '__all__'
        read_only_fields = ['id']
    
    def create(self, validated_data):
        cinema = Cinema.objects.create(**validated_data)
        cinema.save()
        return cinema

class ClassifiesSerializer(serializers.ModelSerializer):
    """
    Serializer for classifies model
    """
    class Meta:
        model = Classifies
        fields = '__all__'
        read_only_fields = ['id']
        
    def create(self, validated_data):
        classifies = Classifies.objects.create(**validated_data)
        classifies.save()
        return classifies

class GenreSerialzer(serializers.ModelSerializer):
    """
    Serializer for Genre model
    """
    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ['id']
    
    def create(self, validated_data):
        genre = Genre.objects.create(**validated_data)
        genre.save()
        return genre
    
class MovieSerializer(serializers.ModelSerializer):
    """
    Serializer for Movie model
    """
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id', 'is_active']
        
    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        movie.save()
        return movie
    
class MovieShowSerializer(serializers.ModelSerializer):
    """
    Serializer for movieshow model
    """
    class Meta:
        model = MovieShow
        fields = '__all__'
        read_only_fields = ['id']
    
    def create(self, validated_data):
        movieshow = MovieShow.objects.create(**validated_data)
        movieshow.save()
        return movieshow