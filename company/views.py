from django.shortcuts import render, redirect
from django.views import View
from .forms import CompanyForm, CreateCompanyForm
from user.models import CustomUser
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
            user = form1.save() 
            company = form.save(commit=False)  
            company.user_id = user.id
            company.save() 
            messages.success(request, f'User Registered Successfully.')
            return redirect('/login')
        else:
            return render(request, self.template_name, {'form1': form1, 'form': form})