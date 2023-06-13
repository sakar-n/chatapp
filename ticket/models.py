from django.db import models
from user.models import CustomUser
from company.models import Companies,Project

# Create your models here.

class Priorities(models.Model):
    priority_id = models.AutoField(primary_key=True)
    company = models.ForeignKey(Companies, null=False, on_delete=models.CASCADE)
    priority_name = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.priority_name
    
class Tickets(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=100, null=False, blank=False )
    message = models.CharField(max_length=384000, null=False, blank=False)
    issued_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    prj = models.ForeignKey(Project, on_delete=models.CASCADE)
    priority = models.ForeignKey(Priorities, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    closed_status = models.BooleanField(default=False)
    due_date = models.DateTimeField(null=False)
    closed_date = models.DateTimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class MessageModel(models.Model):
    message_id = models.AutoField(primary_key=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    message = models.CharField(max_length=384000, null=True, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
class Attachments(models.Model):
    attachment_id =  models.AutoField(primary_key=True)
    file = models.FileField(upload_to="media/", null=True, blank=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)

class MessageAttachments(models.Model):
    attachment_id =  models.AutoField(primary_key=True)
    file = models.FileField(upload_to="media/", null=True, blank=True)
    ticket = models.ForeignKey(Tickets, on_delete=models.CASCADE)
    message = models.ForeignKey(MessageModel, on_delete=models.CASCADE)