from django import forms
from datetime import datetime, timedelta
from .models import Tickets, Attachments, Priorities, MessageModel, MessageAttachments
from company.models import CompanyUser, ForeignUser, Project

class TicketForm(forms.ModelForm):
    subject = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder':'subject', 'class':'form-control'}))
    message = forms.CharField(max_length=384000, required=True, widget=forms.Textarea(attrs={'placeholder':'Enter Message', 'class':'form-control'}))
    prj = forms.ModelChoiceField(queryset=None)
    due_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}), initial=datetime.now() + timedelta(hours=48))
    priority_name = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id', None) 
        self.request = kwargs.pop("request")
        # Retrieve company_id from kwargs
        super().__init__(*args, **kwargs)
        project_ids = [foreign_user.project_id for foreign_user in ForeignUser.objects.filter(user_id=self.request.user)]
        # Filter priorities based on the company_id
        self.fields['prj'].queryset = Project.objects.filter(pk__in=project_ids)

        
        if company_id is not None:
            self.fields['priority_name'].queryset = Priorities.objects.filter(company_id=company_id)

    class Meta:
        model = Tickets
        fields =['subject', 'message', 'priority_name', 'prj', 'due_date']
        
        
class AttachmentForm(forms.ModelForm):
    file = forms.FileField(required=False)
    
    class Meta:
        model = Attachments
        fields = ['file']

class AddPrioritiesForm(forms.ModelForm):
    priority_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class':'form-controller'}))
   
    class Meta:
        model = Priorities
        fields = ['priority_name']


class MessageForm(forms.ModelForm):
    message = forms.CharField(max_length=384000, required=True, widget=forms.TextInput(attrs={'placeholder':'Enter Message', 'class':'form-control form-control-lg'}))
    
    class Meta:
        model = MessageModel
        fields = ['message']
        
class MessageAttachmentForm(forms.ModelForm):
    file = forms.FileField(required=False)
    
    class Meta:
        model = MessageAttachments
        fields = ['file']

