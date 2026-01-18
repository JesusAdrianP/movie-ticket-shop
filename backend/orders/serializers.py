from rest_framework import serializers
from .models import Ticket, Order, Payment

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        read_only_fields = '__all__'
        
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = '__all__'
     
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
    order_date = serializers.DateField()
    
    def validate_tickets(self, value):
        if not value:
            raise serializers.ValidationError(
                "La orden debe contener al menos un ticket"
            )
        return value