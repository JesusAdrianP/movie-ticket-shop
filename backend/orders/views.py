from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.views import APIView
from .serializers import OrderCreateSerializer
from .services import create_order_with_tickets
from rest_framework.response import Response

# Create your views here.
class OrderCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        serializer = OrderCreateSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        
        order = create_order_with_tickets(
            user= request.user,
            order_date= data['order_date'],
            tickets_data= data['tickets'],
            payment_data=data['payment']
        )
        
        return Response( {"order_id": order.id}, status=201)