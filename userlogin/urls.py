from django.urls import path
from .views import *


urlpatterns = [
    path('', Base.as_view(), name='base'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
]