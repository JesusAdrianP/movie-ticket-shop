from django.urls import path
from .views import OrderCreateView, OrderListView, RetrieveOrderView

urlpatterns = [
    path('buy/tickets', OrderCreateView.as_view(), name='buy-tickets'),
    path('my-orders', OrderListView.as_view(), name='list-my-orders'),
    path('my-order/<int:pk>', RetrieveOrderView.as_view(), name='my-order')
]