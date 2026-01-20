from rest_framework import serializers
from .models import City, Cinema, Classifies, Genre, Movie, MovieShow, CinemaRoom

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
    genres = GenreSerialzer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ['id', 'is_active']
        
    def create(self, validated_data):
        movie = Movie.objects.create(**validated_data)
        movie.save()
        return movie
    
class CinemaRoomSerializer(serializers.ModelSerializer):
    """
    Serializer for model Cinema room
    """
    cinema = CinemaSerializer(read_only = True)
    class Meta:
        model = CinemaRoom
        fields = '__all__'
        read_only_fields = ['id']
    
class MovieShowSerializer(serializers.ModelSerializer):
    """
    Serializer for movieshow model
    """
    occupied_seats = serializers.SerializerMethodField()
    room = CinemaRoomSerializer(read_only=True)
    class Meta:
        model = MovieShow
        fields = '__all__'
        read_only_fields = ['id']
        
    def get_occupied_seats(self, obj):
        return list(
            obj.tickets.values_list("seat_number", flat=True)
        )