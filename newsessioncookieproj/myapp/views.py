from django.shortcuts import render,redirect,get_object_or_404
from .forms import SignUpForm
from .models import User


# Create your views here.

def home_view(request):
    return render(request,'myapp/home.html')

def login_view(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        print(f"Username: {uname}\nPassword:{pwd}")
        return redirect('home') 
    return render(request,'myapp/login.html',{'form':form})

def register_view(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'myapp/register.html',{'form':form})