from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom user model admin to display model attributes in admin panel table
    Search users by email
    Only can deactivate user
    """
    
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active')
    search_fields = ('email',)
    
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'password', 'is_active')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('emial', 'password1', 'password2')
        })
    )
    
    editable_fields = ('is_active')
    
    """
    method to add all user fields as readonly except for is_active field
    """
    def get_readonly_fields(self, request, obj = None):
        all_fields = [field.name for field in self.model._meta.fields]
        return [f for f in all_fields if f not in self.editable_fields]