# from typing import Any, Mapping, Optional, Type, Union
from django import forms
from django.forms.utils import ErrorList
from .models import Companies, Project, ProjectUser, CompanyUser, AssiciateCompany, ForeignUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from user.models import CustomUser
        
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'NITV PVT. LTD', 'class':'form-control'}))
    
    class  Meta:
        model = Companies 
        fields= ['company_name']
        
    

class CreateCompanyForm(UserCreationForm):
    username = forms.CharField(max_length=100, required=True)
    email = forms.EmailField( max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': '9876543210','class': 'form-control'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields= ['username', 'email', 'phone', 'password1', 'password2']

class CompanyUpdateForm(forms.ModelForm):
    company_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'ABC PVT. LTD', 'class':'form-control'}))
    
    class  Meta:
        model = Companies 
        fields= ['company_name']
        
class UserUpdateForm(forms.ModelForm):
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': '9876543210','class': 'form-control'}))
    email = forms.EmailField( max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
   
    class Meta:
        model = CustomUser
        fields= ['phone', 'email']
        
class AddProjectForm(forms.ModelForm):
    project_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Project Name','class':'from-control'}))
    
    class Meta:
        model = Project
        fields = ['project_name']
    
class ProjectAssignForm(forms.Form):
    user_id = forms.ModelChoiceField(queryset=CompanyUser.objects.all())

    def __init__(self, *args, **kwargs):
        company_id = kwargs.pop('company_id')
        super(ProjectAssignForm, self).__init__(*args, **kwargs)
        self.fields['user_id'].queryset = CompanyUser.objects.filter(company_id=company_id)
        self.fields['user_id'].label_from_instance = self.get_user_email

    def get_user_email(self, instance):
        return instance.user.email
    
class AssociateCompanyForm(forms.ModelForm):
    company = forms.ModelChoiceField(queryset = Companies.objects.all())
    
    class Meta:
        model = AssiciateCompany
        fields = ['company']
