from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django .views import View
from .forms import ParasiteForm
from user.forms import CreateUserForm
from company.models import Companies
from .models import PasariteUser, ProjectParasite
from django.contrib import messages
from user.models import CustomUser



class HostUserRegister(LoginRequiredMixin, View):
    userform = CreateUserForm
    template_name = 'host_user_creation.html'
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
            PasariteUser.objects.create(company_id=company_id, user_id=user.id)
            messages.success(request, 'User Registered Successfully.')
            return redirect('add_host_user')
        else:
            messages.error(request, form1.errors)
            return render(request, self.template_name, {'form1': form1, "companyname":company_name})

class DisplayHostUser(View):
    template_name = 'display_host_user.html'
    def get(self, request):
        company_name = Companies.objects.get(user_id=request.user.id).company_name
        company_id = Companies.objects.get(user_id=request.user.id)
        users = PasariteUser.objects.filter(company_id=company_id)
        return render(request, self.template_name, {'users':users})

class Parasite_User(View):
    template_name = 'parasite_user.html'
    parasite_user = ParasiteForm
    def get(self, request, project_id, company_id):
        form = self.parasite_user(company_id=company_id)
        parasite_user = ProjectParasite.objects.filter(project_id=project_id)
        return render(request, self.template_name, {'form':form, 'parasite_user':parasite_user})
    
    def post(self, request, project_id, company_id):
        parasite_user = ProjectParasite.objects.filter(project_id=project_id)
        form = self.parasite_user(request.POST, company_id=company_id)
        if form.is_valid():
            email = form.cleaned_data['user_id'].user.email
            user = CustomUser.objects.get(email=email)
            if ProjectParasite.objects.filter(project_id=project_id, user_id=user.id).exists():
                messages.error(request, "This user is Already Assigned to this Project")
                return render(request, self.template_name, {'form':form, 'parasite_user':parasite_user})
            elif ProjectParasite.objects.filter(project_id=project_id).exists():
                messages.error(request, "This project can no longer accept hostuser. Slot not avilable.")
                return render(request, self.template_name, {'form':form, 'parasite_user':parasite_user})               
            else:
                ProjectParasite.objects.create(project_id=project_id, user_id=user.id)
                messages.success(request, "Project Assigned Successfully")
                return render(request, self.template_name,  {'form':form, 'parasite_user':parasite_user})

class Delete_Parasite_User(View):
    def get(self, request, project_id, company_id, user_id):
        parasite_user = ProjectParasite.objects.filter(project_id=project_id, user_id = user_id)
        parasite_user.delete()
        messages.success(request, "User removed Successfully from Project")
        return redirect('parasite_user', project_id, company_id)