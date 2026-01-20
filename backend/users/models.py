from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.password_validation import validate_password

# Create your models here.

#class CustomUserManager
class CustomUserManager(BaseUserManager):
    """
    Model to create managers users for admin panel
    Only requires email and password
    """
    
    def create_user(self, email, password, **extra_fields):
        # create and save new user with given email and passoword
        validate_password(password)
        
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, email, password, **extra_fields):
        #create and save new superuser with given email and password
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        
        user = self.create_user(email=email, password=password, **extra_fields)
        return user

#class CustomUser
class CustomUser(AbstractUser, PermissionsMixin):
    
    """
    Model to create a custom normal user
    requires first_name, last_name, number_phone, email and password
    """
    
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    username = None
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, validators=[validators.MinLengthValidator(8)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()
    
    def __str__(self):
        return f"user email: {self.email}"