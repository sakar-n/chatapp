from django.db import models
from user.models import CustomUser

# Create your models here.

class Priorities(models.Model):
    priority_id = models.AutoField(primary_key=True)
    priority_name = models.CharField(max_length=30, null=False, blank=False)
    
class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, null=False, blank=False )
    message = models.CharField(max_length=384000, null=False, blank=False)
    issued_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #received_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priorities, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=False)
    closed_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Attachments(models.Model):
    attachment_id =  models.AutoField(primary_key=True)
    file = models.FileField(null=False, blank=False, unique=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    


    
