from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length= 15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True) 
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    

    objects = CustomUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
         return self.email

    # def __str__(self):
    #     return self.created_at
class Companies():
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, null=False, default="abc pvt ltd")
    company_email = models.EmailField(unique=True, null=False, default="abc@gmail.com")
    company_phone = models.CharField(max_length= 15)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)