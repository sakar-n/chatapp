from django.urls import path
from .views import CompanyReg

urlpatterns=[
    path('companyreg/', CompanyReg.as_view(), name="companyreg"),
]