from django.shortcuts import render,redirect
from .models import User
from .forms import RegisterForm

# Create your views here.
def home_view(request):
    usname=request.COOKIES.get('uname')
    uspw=request.COOKIES.get('pww')
    return render(request,'myapp/home.html',{'name':usname,'pass':uspw})

def register_view(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'myapp/register.html',{'form':form})

def login_view(request):
    form=RegisterForm()
    if request.method=="POST":
        form=RegisterForm(request.POST)
        uname=request.POST.get('username')
        pwd=request.POST.get('password')
        # print(f"Username: {uname}\nPassword: {pwd}")
        response=redirect('home')
        response.set_cookie('uname',uname)
        response.set_cookie('pww',pwd)
        return response
    return render(request,'myapp/login.html',{'form':form})