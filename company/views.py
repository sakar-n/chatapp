from django.shortcuts import render, redirect
from django.views import View
from .forms import CompanyForm, CreateCompanyForm, CompanyUpdateForm, UserUpdateForm, AddProjectForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Companies
from django.contrib import messages
# Create your views here.


class CompanyReg(View):
    company_form = CompanyForm
    reg_form = CreateCompanyForm
    template_name = "register.html"
    
    def get(self, request):
        form = self.company_form()
        form1 = self.reg_form()
        return render(request, self.template_name, {'form1': form1,
                                                    'form':form})
    
    def post(self, request):
        form1 = self.reg_form(request.POST)
        form = self.company_form(request.POST)
        
        if form1.is_valid() and form.is_valid():
            compnay_input = form.cleaned_data['company_name']
            if Companies.objects.filter(company_name=compnay_input).exists():
                messages.error(request, 'Company with this name already exist.')
                return render(request, self.template_name, {'form1': form1, 'form': form})
            else:
                user = form1.save() 
                company = form.save(commit=False)  
                company.user_id = user.id
                company.save() 
                messages.success(request, 'User Registered Successfully.')
                return redirect('/login')
        else:
                return render(request, self.template_name, {'form1': form1, 'form': form})
        
class CompanyUpadate(View):
    companydetails = UserUpdateForm
    companyname = CompanyUpdateForm
    template_name = 'companyupdate.html'
    def get(self, request):
            company_data = Companies.objects.get(user=request.user)
            form2 = self.companyname()
            user_data = {   
                'phone': request.user.phone,
                'email':request.user.email,

            }
            form1 = self.companydetails(initial=user_data)
            form2.fields['company_name'].initial = company_data.company_name

            # Render the template with the forms
            return render(request, self.template_name, {'form1': form1, 'form2': form2})
        
    def post(self, request):
            form2 = self.companyname(request.POST, instance=request.user)
            form1 = self.companydetails(request.POST, instance=request.user )
            if form1.is_valid() and form2.is_valid():
                form1.save()
                form2.save()
                messages.success(request, 'Your profile has been updated Sccessfully')
                return redirect('index')
            else:
                messages.error(request, 'Invalid Inputs')
                return render(request, self.template_name, {'form1':form1, 'form2':form2})
            
class AddProject(LoginRequiredMixin, View):
    projectform = AddProjectForm
    template_name = "project.html"
    def get(self, request):
        return render(request, self.template_name, {'form':self.projectform})
    
    def post(self, request):
        form = self.projectform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Project Added Successfully")
            return redirect('project')
        else:
            messages.error(request, 'Project Cannot Be Added')
            return render(request, self.template_name, {'form':form})
