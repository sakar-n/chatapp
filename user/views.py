from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth import authenticate, login 
from django.views import View
from django.contrib import messages
from .forms import CreateUserForm, UserLoginForm, UserUpdateForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from company.forms import CompanyForm
from company.models import Companies, CompanyUser

class Index(LoginRequiredMixin, View):
    template_name="index.html"
    def get(self, request):
        company_name = Companies.objects.get(user_id=request.user.id).company_name
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        users = CompanyUser.objects.filter(company_id=company_id)
        context = {"users": users,
                   "companyname": company_name,
                   }
        return render(request, self.template_name, context)
    
    

    
class Register(LoginRequiredMixin, View):
    userform = CreateUserForm
    template_name = 'user_register.html'
    def get(self, request):
        company_name = Companies.objects.get(user_id=request.user.id).company_name
        form1 = self.userform()
        return render(request, self.template_name, {'form1': form1, "companyname":company_name})
    
    def post(self, request):
        form1 = self.userform(request.POST)
        company_name = Companies.objects.get(user_id=request.user.id).company_name
        if form1.is_valid():
            user = form1.save()
            company_id = Companies.objects.get(user_id=request.user.id).company_id
            CompanyUser.objects.create(user_id=user.id, company_id=company_id)
            messages.success(request, f'User Registered Successfully.')
            return redirect('index')
        else:
            return render(request, self.template_name, {'form1': form1, "companyname":company_name})

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
    
class UserUpdate(LoginRequiredMixin, View):
    updateform = UserUpdateForm
    template_name = 'userupdate.html'

    def get(self, request):
        user_data = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email,
            'phone': request.user.phone,
        }
        form = self.updateform(initial=user_data)
        return render(request, self.template_name, {"form":form})

