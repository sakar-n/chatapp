from django.shortcuts import render, redirect
from .forms import UserForm,UserRegister
from django.views.generic import View, TemplateView
from django.contrib.auth.views import LoginView


# Create your views here.
class Base(TemplateView):
    template_name = "base.html"

class Login(LoginView):
    form = UserForm
    template_name = "login.html"
    
    def get(self, request): 
        return render(request, self.template_name, context={'form': self.form})
    
class Register(View):
    template_name = "register.html"
    form = UserRegister
    
    def get(self,request):
        return render(request, self.template_name, {'form': self.form})
    def post(self, request):
        if request.method == "POST":
            form = UserRegister(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "login.html")                
        return render(request, self.template_name, {'form': self.form})