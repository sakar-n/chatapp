from django.urls import path
from .views import Register, Login, Index, Logout
from django.contrib.auth.decorators import login_required

urlpatterns=[
    path('', login_required(Index.as_view()), name='index'),
    path("user_register/", login_required(Register.as_view()), name='user_register'),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout")
]