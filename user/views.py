from django.shortcuts import render,redirect, get_object_or_404, HttpResponse
from django.views import View
from django.contrib import messages
from .forms import CreateUserForm, UserLoginForm, UserUpdateForm
from .models import CustomUser
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login,  logout, authenticate
from company.models import Companies, CompanyUser, Project, AssiciateCompany, ProjectUser
from ticket.models import Tickets
from django.contrib.auth.views import PasswordResetView,PasswordResetCompleteView,PasswordResetConfirmView,PasswordResetDoneView

class Index(LoginRequiredMixin, View):
    template_name="index.html"
    template_name1="userindex.html"
    def get(self, request):
        try:
            company_name = Companies.objects.get(user_id=request.user.id).company_name
            company_id = Companies.objects.get(user_id=request.user.id)
            users = CompanyUser.objects.filter(company_id=company_id)
            project = Project.objects.filter(company_id=company_id).count()
            project_id = Project.objects.filter(company_id = company_id)
            received_tickets = Tickets.objects.filter(prj_id__in=project_id).count()
            associate_companies = AssiciateCompany.objects.filter(company_id=company_id)
            projects = [associate_company.project for associate_company in associate_companies]
            issued_tickets = Tickets.objects.filter(prj_id__in=projects).count()
            context = { "users": users,
                        "companyname": company_name,
                        "user_count": users.count(),
                        "project":project,
                        "received_tickets": received_tickets,
                        "issued_tickets": issued_tickets,
                        "active_link":"index",
                   }
            return render(request, self.template_name, context)
        except:
            user_project_id =  ProjectUser.objects.filter(user_id=request.user.id).values_list('project_id', flat=True)
            rec_tickets = Tickets.objects.filter(prj_id__in=user_project_id).count()
            tickets = Tickets.objects.filter(issued_by_id=request.user.id)
            return render(request, self.template_name1, {'tickets':tickets, 'rec_tickets':rec_tickets, 'ticket_count':tickets.count(), "active_link":"index"})

    

    
class Register(LoginRequiredMixin, View):
    userform = CreateUserForm
    template_name = 'user_register.html'
    def get(self, request):
        company_name = Companies.objects.get(user_id=request.user.id).company_name
        form1 = self.userform()
        return render(request, self.template_name, {'form1': form1, "companyname":company_name, 'active_link':"addEmployee"})
    
    def post(self, request):
        form1 = self.userform(request.POST)
        company_name = Companies.objects.get(user_id=request.user.id).company_name
        if form1.is_valid():
            user = form1.save()
            company_id = Companies.objects.get(user_id=request.user.id).company_id
            CompanyUser.objects.create(user_id=user.id, company_id=company_id)
            messages.success(request, 'User Registered Successfully.')
            return redirect('index')
        else:
            messages.error(request, form1.errors)
            return render(request, self.template_name, {'form1': form1, "companyname":company_name})

class Login(View):
    form_name = UserLoginForm
    template_name = 'login.html'
    
    def get(self, request):
        form = self.form_name()
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form})
    
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
                    if not CustomUser.objects.filter(email=email).exists():
                        messages.error(request, "Invalid email. Please enter a valid email address.")
                    elif not CustomUser.objects.filter(email=email, password=password).exists():
                        messages.error(request, "Incorrect password. Please enter the correct password.")

            return render(request, self.template_name, {'form': self.form_name})
    

class Logout(LoginRequiredMixin, View):
    template_name = 'login.html'
    def get(self, request):
        logout(request)
        return redirect('login')
    
class UserUpdate(LoginRequiredMixin, View):
    updateform = UserUpdateForm
    template_name = 'userupdate.html'

    def get(self, request, user_id):
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        user1 = get_object_or_404(CustomUser, id=user_id)
        user_data = {
            'first_name': user1.first_name,
            'last_name': user1.last_name,
            'email': user1.email,
            'phone': user1.phone,
        }
        form = self.updateform(initial=user_data)
        if get_object_or_404(CompanyUser, user_id = user1, company_id = company_id):
            return render(request, self.template_name, {"form": form, "user": user1})
        
      
    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = self.updateform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User Updated Successfully")
            return redirect('index')
        
        else:
            return render(request, self.template_name, {"form": form, "user": user})
        
class SelfUpdate(LoginRequiredMixin, View):
    updateform = UserUpdateForm
    template_name = 'userupdate.html'

    def get(self, request, user_id):
        user1 = get_object_or_404(CustomUser, id=user_id)
        user_data = {
            'first_name': user1.first_name,
            'last_name': user1.last_name,
            'email': user1.email,
            'phone': user1.phone,
        }
        form = self.updateform(initial=user_data)
        return render(request, self.template_name, {"form": form, "user": user1})
        
      
    def post(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        form = self.updateform(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "User Updated Successfully")
            return redirect('index')
        
        else:
            return render(request, self.template_name, {"form": form, "user": user})
        
# class UserDelete(LoginRequiredMixin, View):
#     template_name = "deleteuser.html"
#     def get(self, request, user_id):
#         user = get_object_or_404(CustomUser, id= user_id)
#         company_id = Companies.objects.get(user_id=request.user.id).company_id
#         if get_object_or_404(CompanyUser, user_id = user, company_id = company_id):
#            return render(request, self.template_name, {"user": user})
       
        
#     def post(self, request, user_id):
#         user = get_object_or_404(CustomUser, id= user_id)
#         if request.method == "POST":
#             user.delete()
#             messages.success(request, "User deleted successfully")
#             return redirect("index")
#         else:
#             return render(request, self.template_name, {"user": user})
    
class UserDelete(LoginRequiredMixin, View):
           
    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id = user_id)
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        print(company_id)
        print(user)
        user.delete()
        messages.success(request, "User deleted successfully")
        return redirect("index")

