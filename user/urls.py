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
    path('userdelete/delete/<int:user_id>', UserDelete.as_view(), name='delete_user'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',html_email_template_name='reset_email.html'),name="reset_password"),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name="reset_password_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name="reset_password_confirm"),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name="password_reset_complete"),
]
