from django.urls import path
from .views import Register, Login, base

urlpatterns=[
    path("", base, name='base'),
    path("register/", Register.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
]