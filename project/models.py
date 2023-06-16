from django.db import models
from company.models import Companies, Project
from user.models import CustomUser
# Create your models here.

class PasariteUser(models.Model):
    company = models.ForeignKey(Companies, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

class ProjectParasite(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)