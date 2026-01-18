from django.urls import path
from .views import OrderCreateView

urlpatterns = [
    path('buy/tickets', OrderCreateView.as_view(), name='buy-tickets'),
]