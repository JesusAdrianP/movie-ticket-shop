from django.db import models
from users.models import CustomUser
from movies.models import MovieShow

# Create your models here.

# Order model
class Order(models.Model):
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='orders', null=False)
    
    def __str__(self):
        return f"Order id: {self.pk} User email: {self.user_id.email} Total amount: {self.total_amount}"
    
# Ticket model
class Ticket(models.Model):
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    seat_number = models.CharField(max_length=10, blank=False, null=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='tickets')
    movie_show_id = models.ForeignKey(MovieShow, on_delete=models.CASCADE, related_name='tickets')
    
    def __str__(self):
        return f"Ticket id: {self.pk} seat number: {self.seat_number} Unit price: {self.unit_price}"
    
#payment model
class Payment(models.Model):
    #payment method choices
    PAYMENT_METHOD_CHOICES = [
        ('CREDIT_CARD', 'Tarjeta de crédito'),
        ('DEBIT_CARD', 'Tarjeta de débito'),
        ('PSE', 'PSE')
    ]
    
    #Status Choices
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('APPROVED', 'Aprovado'),
        ('REJECTED', 'Rechazado')
    ]
    
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, blank=False, null=False)
    card_holder_name = models.CharField(max_length=100, blank=False, null=False)
    card_last_four_digits = models.CharField(max_length=4, blank=False, null=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='payments', null=False, blank=False)
    
    def __str__(self):
        return f"Payment id: {self.pk} Order id:{self.order_id.pk} Status: {self.status}"