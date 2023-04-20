from django.urls import path
from .views import CompanyReg

urlpatterns=[
    path('register/', CompanyReg.as_view(), name="register"),
]