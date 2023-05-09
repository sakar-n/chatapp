from django.urls import path
from .views import CompanyReg, CompanyUpadate, AddProject, ProjectDelete, ProjectUpdate, AddProjectUser
urlpatterns=[
    path('register/', CompanyReg.as_view(), name="register"),
    path('companyupdate/', CompanyUpadate.as_view(), name="companyupdate"),
    path('project/', AddProject.as_view(), name='project'),
    path('projectdelete/<int:project_id>', ProjectDelete.as_view(), name='delete_project'),
    path('projectupdate/<int:project_id>', ProjectUpdate.as_view(), name='project_update'),
    path('addprojectuser/<int:project_id>/<int:company_id>/', AddProjectUser.as_view(), name='project_user'),
]