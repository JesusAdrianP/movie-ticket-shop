from rest_framework import serializers
from .models import Ticket, Order, Payment
from movies.serializers import MovieShowSerializer

class TicketSerializer(serializers.ModelSerializer):
    #movie_show_id = MovieShowSerializer(read_only=True)
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = [ field.name for field in Ticket._meta.fields]
        
class OrderSerializer(serializers.ModelSerializer):
    """
    Serializer for Order model
    Retrieves info from order instance and some info from foreing keys
    """
    seats = serializers.SerializerMethodField()
    movie_name = serializers.SerializerMethodField()
    city_name = serializers.SerializerMethodField()
    cinema_name = serializers.SerializerMethodField()
    show_time = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    ticket_unit_price =serializers.SerializerMethodField()
    room_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Order
        fields = ['id', 'movie_name', 'city_name', 'cinema_name', 'show_time', 'room_name','seats', 'ticket_unit_price', 'total_amount', 'status', 'created_at']
        read_only_fields = [ field.name for field in Order._meta.fields]
        
    def safe_getattr(self, obj, attr_path, default=None):
        """
        Securely access chained attributes
        """
        for attr in attr_path.split('.'):
            obj = getattr(obj, attr, None)
            if obj is None:
                return default
        
        return obj
    
    """
    Get seats number from tickets
    """
    def get_seats(self, obj):
        return [ticket.seat_number for ticket in obj.tickets.all()]
    
    """
    Get room of purchased tickets
    """
    def get_room_name(self, obj):
        first_ticket =  obj.tickets.first()
        return self.safe_getattr(first_ticket, 'movie_show_id.room.room_name')
    
    """
    Get price of a ticket
    """
    def get_ticket_unit_price(self, obj):
        first_ticket = obj.tickets.first()
        if first_ticket:
            return first_ticket.unit_price
    
    """
    Get Payment status
    """
    def get_status(self, obj):
        payment = obj.payments.first()
        if payment:
            return payment.status
        return None
    
    """
    Get movie name
    """
    def get_movie_name(self, obj):
        first_ticket = obj.tickets.first()
        return self.safe_getattr(first_ticket, 'movie_show_id.movie_id.movie_name')
    
    """
    Get cinema name of movie show
    """
    def get_cinema_name(self, obj):
        first_ticket = obj.tickets.first()
        return self.safe_getattr(first_ticket, 'movie_show_id.room.cinema.cinema_name')
    
    """
    Get city name of the movie show
    """
    def get_city_name(self, obj):
        first_ticket = obj.tickets.first()
        return self.safe_getattr(first_ticket, 'movie_show_id.room.cinema.city_id.city_name')
    
    """
    Get movie show date
    """
    def get_show_time(self, obj):
        first_ticket = obj.tickets.first()
        return self.safe_getattr(first_ticket, 'movie_show_id.show_date')
    
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = [ field.name for field in Payment._meta.fields]
     
class TicketCreateSerializer(serializers.Serializer):
    movie_show_id = serializers.IntegerField()
    seat_number = serializers.CharField(max_length=10)
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2)
    
class PaymentCreateSerializer(serializers.Serializer):
    payment_method = serializers.CharField(max_length=20)
    card_holder_name = serializers.CharField(max_length=100)
    card_last_four_digits = serializers.CharField(max_length=4)

class OrderCreateSerializer(serializers.Serializer):
    tickets = TicketCreateSerializer(many=True)
    payment = PaymentCreateSerializer()
    
    def validate_tickets(self, value):
        if not value:
            raise serializers.ValidationError(
                "La orden debe contener al menos un ticket"
            )
        return value