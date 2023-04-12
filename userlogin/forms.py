from django import forms 
from .models import UserModels

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=30, required=True, widget=forms.EmailInput(attrs={"placeholder":"Enter Valid Email", "class":"form-control"}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={"placeholder":"Password", "class":"form-control"}))
        
    class Meta:
        model = UserModels
        fields = ['email','password']

class UserRegister(forms.ModelForm):
    first_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={"placeholder":"", "class":"form-control"}))
    last_name = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={"placeholder":"", "class":"form-control"}))
    number = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={"placeholder":"", "class":"form-control"}))
    email = forms.EmailField(max_length=30, required=True, widget=forms.EmailInput(attrs={"placeholder":"", "class":"form-control"}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={"placeholder":"", "class":"form-control"}))
    
    class Meta:
        model = UserModels
        fields = ["first_name", "last_name", "number", "email", "password", "password"]
