from django import forms
from .models import Companies
from django.contrib.auth.forms import UserCreationForm
from user.models import CustomUser
        
class CompanyForm(forms.ModelForm):
    company_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'NITV PVT. LTD', 'class':'form-control'}))
    
    class  Meta:
        model = Companies 
        fields= ['company_name']
        
    

class CreateCompanyForm(UserCreationForm):
    email = forms.EmailField( max_length=50, required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': '9876543210','class': 'form-control'}))
    password1 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    password2 = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields= ['email', 'phone', 'password1', 'password2']
