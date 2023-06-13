from django.urls import path
from django.contrib.auth.decorators import login_required 
from .views import CompanyReg, CompanyUpadate, AddProject, ProjectDelete, ProjectUpdate, AddProjectUser, Associate_Company, ProejctAcceptance, RejectProject, Foreign_User, DeleteProjectUser, CancelProjectReq, DeleteForeignUser
urlpatterns=[
    path('register/', login_required(CompanyReg.as_view()), name="register"),
    path('companyupdate/', CompanyUpadate.as_view(), name="companyupdate"),
    path('project/', AddProject.as_view(), name='project'),
    path('projectdelete/<int:project_id>', ProjectDelete.as_view(), name='delete_project'),
    path('projectupdate/<int:project_id>', ProjectUpdate.as_view(), name='project_update'),
    path('addprojectuser/<int:project_id>/<int:company_id>/', AddProjectUser.as_view(), name='project_user'),
    path('deleteprojectuser/<int:project_id>/<int:company_id>/<int:user_id>/', DeleteProjectUser.as_view(), name='deleteproject_user'),
    path('requestcompany/<int:project_id>/', Associate_Company.as_view(), name='associate_company'),
    path('projectacceptance/', ProejctAcceptance.as_view(), name='project_accept'),
    path('project/decline/<int:id>', RejectProject.as_view(), name='decline_project'),
    path('project/cancel/<int:project_id>', CancelProjectReq.as_view(), name='cancel_project_request'),
    path('project/add/<int:id>/<int:company_id>/<int:project_id>', Foreign_User.as_view(), name='foreign_user'),
    path('project/delete/<int:id>', DeleteForeignUser.as_view(), name='delete_foreign_user'),
]