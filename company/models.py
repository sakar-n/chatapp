from django.db import models
from user.models import CustomUser
# Create your models here.
class Companies(models.Model):
    company_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=225, null=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now_add=True)
    
class CompanyUser(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null= False)
    
class ProjectUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null= False)

class AssiciateCompany(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=False)