from django.urls import path
from .views import Register, Login, Index, Logout, UserUpdate, UserDelete
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('', login_required(Index.as_view()), name='index'),
    path("user_register/", login_required(Register.as_view()), name='user_register'),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path('userupdate/<int:user_id>', UserUpdate.as_view(), name='update_user'),
    path('userdelete/<int:user_id>', UserDelete.as_view(), name='delete_user'),
]
