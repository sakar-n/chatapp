from django.urls import path
from .views import CompanyReg, CompanyUpadate

urlpatterns=[
    path('register/', CompanyReg.as_view(), name="register"),
    path('companyupdate/', CompanyUpadate.as_view(), name="companyupdate")
]