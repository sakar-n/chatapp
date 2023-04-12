from django.shortcuts import render
from .forms import UserForm,UserRegister

# Create your views here.
def base(request):
    return render(request, 'base.html')

def login(request):
    context = {}
    form = UserForm
    context['form']= form
    return render(request, 'login.html', context)

def register(request): 
    context = {}
    form = UserRegister
    context['form']= form
    return render(request, 'register.html', context)