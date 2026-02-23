from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import SignUpForm
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'myapp/home.html')

def register(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'myapp/register.html',{'form':form})


@login_required
def employee(request):
    emp=User.objects.all()
    return render(request,'myapp/emplist.html',{'emp':emp})

@login_required
def addemp(request):
    return render(request,'myapp/addemp.html')


def logout_view(request):
    logout(request)
    return render(request,'myapp/logout.html')

def delete(request,pk):
    emp=User.objects.get(pk=pk)
    emp.delete()
    return redirect('emplist')
   

def edit(request,pk):
    emp=User.objects.get(pk=pk)
    if request.method=="POST":
        form=SignUpForm(request.POST,instance=emp)
        if form.is_valid():
            form.save()
            return redirect('emplist')
    else:
        form=SignUpForm(instance=emp)
    return render(request,'myapp/edit.html',{'form':form})

def view(request,pk):
    emp=User.objects.get(pk=pk)
    return render(request,'myapp/view.html',{'emp':emp})