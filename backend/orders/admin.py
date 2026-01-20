from django.contrib import admin
from .models import Order, Ticket, Payment

# Register your models here.
@admin.register(Order)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'total_amount', 'created_at')
    search_fields = ('user_id__first_name','user_id__last_name', 'user_id__email', 'id')
    readonly_fields = ("created_at",)
admin.site.register(Ticket)
admin.site.register(Payment)