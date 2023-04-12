from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class UserModels(AbstractBaseUser):
    first_name = models.CharField(max_length=15, blank=True, null=True)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=30, blank=True, null=True)
    email = models.EmailField(unique=True) 
    number = models.PositiveIntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["number"]
