from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import CompanyForm, CreateCompanyForm, CompanyUpdateForm, UserUpdateForm, AddProjectForm, ProjectAssignForm
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Companies, Project, CompanyUser, ProjectUser
from django.contrib import messages
from user.models import CustomUser
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
        company_id = Companies.objects.get(user_id=request.user.id)
        projects = Project.objects.filter(company_id=company_id).all()
        return render(request, self.template_name, {'form':self.projectform, "projects":projects})
    
    def post(self, request):
        form = self.projectform(request.POST)
        company_id = Companies.objects.get(user_id=request.user.id).company_id
        projects = Project.objects.filter(company_id=company_id)
        if form.is_valid():
            unsaveform = form.save(commit=False)
            unsaveform.company_id = company_id
            unsaveform.save()
            messages.success(request, "Project Added Successfully")
            return redirect('project')
        else:
            messages.error(request, 'Project Cannot Be Added')
            return render(request, self.template_name, {'form':form, 'projects':projects})

class ProjectDelete(View):
    template_name = "deleteuser.html"
    def get(self, request, project_id):
        project = get_object_or_404(Project, project_id = project_id)
        return render(request, self.template_name, {"project": project})
       
        
    def post(self, request, project_id):
        project = get_object_or_404(Project, project_id = project_id)
        if request.method == "POST":
            project.delete()
            messages.success(request, "Project deleted successfully")
            return redirect("project")
        else:
            return render(request, self.template_name, {"project": project})
        
class ProjectUpdate(View):
    template_name = 'projectupdate.html'
    update_form = AddProjectForm
    def get(self, request, project_id):
        project = get_object_or_404(Project, project_id=project_id) 
        form_data ={
            'project_name':project.project_name,
        }
        form = self.update_form(initial=form_data)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request, project_id):
        project = get_object_or_404(Project, project_id = project_id)
        form = self.update_form(request.POST, instance=project)
        if form.is_valid():
                    form.save()
                    messages.success(request, "Project Updated Successfully")
                    return redirect('project')
        else:
            return render(request, self.template_name,{'form':form})
        
class AddProjectUser(View):
    template_name = "projectuser.html"
    user_form = ProjectAssignForm

    def get(self, request, project_id, company_id):
        form = self.user_form(company_id=company_id)
        project = get_object_or_404(Project, project_id=project_id)
        return render(request, self.template_name, {'project': project, 'form': form})

    def post(self, request, project_id, company_id):
        form = self.user_form(request.POST, company_id=company_id)
        project = get_object_or_404(Project, project_id=project_id).project_id
        if form.is_valid():
            email = form.cleaned_data['user_id'].user.email
            user = CustomUser.objects.get(email=email)
            if ProjectUser.objects.filter(project_id=project_id, user_id=user.id).exists():
                messages.error(request, "This user is Already Assigned to this Project")
                return render(request, self.template_name, {'project': project, 'form': form})
            else:
                ProjectUser.objects.create(project_id=project, user_id=user.id)
                messages.success(request, "Project Assigned Successfully")
                return redirect('project')
        else:
            messages.error(request, "Invalid Input")
            return render(request, self.template_name, {'project': project, 'form': form})
    