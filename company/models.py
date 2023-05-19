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

    def __str__(self):
        return self.company_name
        
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
    
    def __str__(self):
        return self.user.email
    
class ProjectUser(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null= False)

class AssiciateCompany(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)
    company = models.ForeignKey(Companies, on_delete=models.CASCADE, null=False)
    is_active = models.BooleanField(default=False)
    
class ForeignUser(models.Model):
    associate_company = models.ForeignKey(AssiciateCompany, on_delete=models.CASCADE, null=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False)