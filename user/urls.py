from django.urls import path
from .views import Register, Login, Index 
from . import views
urlpatterns=[
    path("", Index.as_view(), name='base'),
    path("register/", Register.as_view(), name='register'),
    path("login/", Login.as_view(), name="login"),
]