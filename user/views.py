from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.views import View
from django.contrib import messages
from .forms import CreateUserForm, UserLoginForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.http import Http404

class Index(LoginRequiredMixin, View):
    template_name="index.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    

    
class Register(View):
    form_class = CreateUserForm
    template_name = 'register.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Save user to database
            form.save()
            messages.success(request, f'Your account has been Created. Now You can login')
            return redirect('login') 
        else:
            return render(request, self.template_name, {'form': form})

class Login(View):
    form_name = UserLoginForm
    template_name = 'login.html'
    
    def post(self, request):
            form = self.form_name(request.POST)
            if form.is_valid():                
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('index') 
                else:
                    messages.error(request, "Invalid username or Password")  
            else:
                messages.error(request, "Invalid username or Password")
            return render(request, self.template_name, {'form': self.form_name})
    
    def get(self, request):
        form = self.form_name()
        return render(request, self.template_name, {'form': form})

class Logout(LoginRequiredMixin, View):
    template_name = 'login.html'
    def get(self, request):
        logout(request)
        return redirect('login')
