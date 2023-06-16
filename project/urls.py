from django .urls import path
from .views import Parasite_User, HostUserRegister, DisplayHostUser, Delete_Parasite_User
urlpatterns = [
    path('parasite_user/<int:project_id>/<int:company_id>', Parasite_User.as_view(), name='parasite_user'),
    path('add_host_user/', HostUserRegister.as_view(), name='add_host_user'),
    path('displaying_host_user/', DisplayHostUser.as_view(), name='displaying_host_user'),
    path('Delete_Parasite_User/<int:project_id>/<int:company_id>/<int:user_id>', Delete_Parasite_User.as_view(), name='delete_parasite_user'),
]
