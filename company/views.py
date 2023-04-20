from django.shortcuts import render, redirect
from django.views import View
from .forms import CompanyForm
from user.forms import CreateUserForm
# Create your views here.


class CompanyReg(View):
    company_form = CompanyForm
    reg_form = CreateUserForm
    template_name = "register.html"
    
    def get(self, request):
        form = self.company_form()
        form1 = self.reg_form()
        return render(request, self.template_name, {'form': form,
                                                    'form1':form1})
    
    def post(self, request):
        form = self.company_form(request.POST)
        form1 = self.reg_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
        else:
            return render(request, self.template_name, {'form': form,
                                                        'form1': form1})
    
        