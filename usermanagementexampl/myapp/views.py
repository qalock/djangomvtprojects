from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

# @login_required
def home(request):
    return render(request,'myapp/home.html')

def login_view(request):
    return render(request,'myapp/login.html')

def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Successfull Please Login")
            return redirect('home')
        
    else:
        form=RegistrationForm()
    return render(request,'myapp/register.html',{'form':form})

