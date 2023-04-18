from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


# class UserRegisterForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}))
#     last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}))
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
#     password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
#     Confirm_password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    

#     class Meta:
#         model = CustomUser
#         fields= ['first_name', 'last_name', 'email', 'password']

class CreateUserForm(UserCreationForm):
    
    first_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'First Name', 'class':'form-control'}))
    last_name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder':'Last Name', 'class':'form-control'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
    # password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    # Confirm_password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields= ['first_name', 'last_name', 'email', 'phone']
    

class UserLoginForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'abc@email.com', 'class':'form-control'}))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password','class': 'form-control'}))
    
    class Meta:
        model = CustomUser
        fields = ['email', 'password']