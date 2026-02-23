from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignUpForm
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,'myapp/home.html')

@login_required
def java_exam_view(request):
    return render(request,'myapp/javaexam.html')

def logout_view(request):
    logout(request)
    return render(request,'myapp/logout.html')

def python_exam_view(request):
    return render(request,'myapp/pythonexam.html')

def register(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'myapp/register.html',{'form':form})