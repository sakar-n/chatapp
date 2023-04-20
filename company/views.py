from django.shortcuts import render, redirect
from django.views import View
from .forms import CompanyForm, CompanyRegForm
# Create your views here.

class CompanyReg(View):
    regform = CompanyRegForm
    template_name = "companyreg.html"
    
    def get(self, request):
        form = self.regform()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.regform(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
        else:
            return render(request, self.template_name, {'form': form})
    
        
    