from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser

class CompanyRegForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields= ['email', 'phone', 'password1', 'password2']
class CompanyForm(forms.Form):
    class Meta:
        model = CustomUser
        fields= ['company_name']
        
        