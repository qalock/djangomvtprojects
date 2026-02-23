from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def employee(request):
    emp=Employee.objects.all()
    return render(request,'imgapp/employee.html',{'emplist':emp})


def register(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('emplist')
    return render(request,'imgapp/register.html',{'form':form})