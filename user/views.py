from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login 
from django.views import View
from django.contrib import messages
from .forms import CreateUserForm, UserLoginForm
from .models import CustomUser


class Index(View):
    template_name = 'base.html'
    def get(self, request):
        return render(request, self.template_name)
        

class Register(View):
    form_class = CreateUserForm
    template_name = 'register.html'
    
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # Save user to database
            form.save()
            return redirect('login') 
        else:
            return render(request, self.template_name, {'form': form})

class Login(View):
    form_name = UserLoginForm
    template_name = 'login.html'
    
    def post(self, request, *args, **kwargs):
            print("........................post")
            form = self.form_name(request.POST)
            if form.is_valid():
                print("........................valid")
                
                email = request.POST['email']
                password = request.POST['password']
                user = authenticate(request, email=email, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('/') 
                else:
                    messages.error(request, "Invalid username or Password")  
            else:
                messages.error(request, "Invalid username or Password")
            return render(request, self.template_name, {'form': self.form_name})
    
    def get(self, request):
        form = self.form_name()
        return render(request, self.template_name, {'form': form})
    