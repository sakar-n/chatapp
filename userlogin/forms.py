from django import forms 
from .models import UserModels

class UserForm(forms.ModelForm):
    email = forms.EmailField(max_length=30, required=True, widget=forms.EmailInput(attrs={"placeholder":"Enter Valid Email", "class":"form-control"}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={"placeholder":"Password", "class":"form-control"}))
        
    class Meta:
        model = UserModels
        fields = ['email','password']

class UserRegister(forms.ModelForm):
    
    class Meta:
        model = UserModels
        fields = "__all__"
