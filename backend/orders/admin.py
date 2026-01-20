from django.contrib import admin
from .models import Order, Ticket, Payment

# Register your models here.
@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    """
    Custom movieShow model admin to display model attributes in admin panel table
    Only for read attributes
    """
    list_display = ('id', 'user_id', 'total_amount', 'created_at')
    search_fields = ('user_id__first_name','user_id__last_name', 'user_id__email', 'id')
    
    def get_readonly_fields(self, request, obj = None):
        return [field.name for field in self.model._meta.fields]
    
@admin.register(Ticket)
class TicketModelAdmin(admin.ModelAdmin):
    """
    Custom Ticket model admin to display model attributes in admin panel table
    And search tickets by user info like email or name
    Only for read attributes
    """
    list_display = ('id', 'seat_number', 'movie_show_id', 'order_id')
    search_fields = ('order_id__user_id__email', 'order_id__user_id__first_name', 'order_id__user_id__last_name')
    
    def get_readonly_fields(self, request, obj = None):
        return [field.name for field in self.model._meta.fields]

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
    """
    Custom Payment model admin to display model attributes in admin panel table
    filter by status and payment_method and search by user email
    Only for read attributes
    """
    list_display = ('order_id__user_id__email', 'payment_method', 'status')
    search_fields = ('order_id__user_id__email',)
    list_filter = ('status', 'payment_method')
    
    def get_readonly_fields(self, request, obj = None):
        return [field.name for field in self.model._meta.fields]