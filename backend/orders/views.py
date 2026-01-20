from django.db import transaction
from rest_framework import permissions, generics
from rest_framework.views import APIView
from .serializers import OrderCreateSerializer, OrderSerializer, TicketSerializer
from .services import create_order_with_tickets, send_order_confirmation_email
from rest_framework.response import Response
from .models import Order, Ticket
from django.db.models import Prefetch

# Create your views here.
class OrderCreateView(APIView):
    """
    View to create and pay new order
    POST: Returns a Json with order_id and status code 201
    Require JWT authentication
    """
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = OrderCreateSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        
        #Creating data with info sent by user
        order = create_order_with_tickets(
            user= request.user,
            tickets_data= data['tickets'],
            payment_data=data['payment']
        )
        
        #If transaction is success, send notification email
        transaction.on_commit(
            lambda: send_order_confirmation_email(order)
        )
        
        return Response( {"order_id": order.id}, status=201)

class OrderListView(generics.ListAPIView):
    """
    View to retrieve all orders of authenticated user
    GET: Return list of Json with order info:
      -id
      -movie_name
      -city_name
      -cinema_name
      -show_time
      -room_name
      -seats ej: ["D4","D5","D6"]
      -ticket_unit_price
      -total_amount
      -status ej: "APPROVED"
      -created_at
    Require JWT Authentication
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        user = self.request.user
        queryset = Order.objects.filter(user_id = user.id)
        return queryset
    
class RetrieveOrderView(generics.RetrieveAPIView):
    """
    View to retrieve info from specific order
    GET: Return JSon with order info:
      -id
      -movie_name
      -city_name
      -cinema_name
      -show_time
      -room_name
      -seats ej: ["D4","D5","D6"]
      -ticket_unit_price
      -total_amount
      -status ej: "APPROVED"
      -created_at
    Require JWT Authentication
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OrderSerializer
    
    def get_queryset(self):
        user = self.request.user
        
        #Obtaining queryset tickets with needed data
        tickets_qs = Ticket.objects.select_related(
            'movie_show_id__movie_id', #Movie
            'movie_show_id__room__cinema', #cinema
            'movie_show_id__room__cinema__city_id' #city
        )
        
        queryset = Order.objects.prefetch_related(Prefetch( 'tickets', queryset=tickets_qs)).filter(user_id = user.id)
        return queryset