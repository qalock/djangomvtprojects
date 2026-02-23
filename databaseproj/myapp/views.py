from django.shortcuts import render,redirect,get_object_or_404
from .models import Employeee
from .forms import EmployeeForm
from django.db.models import Q

# Create your views here.
def employees(request):
    query=request.GET.get('q')
    employee=Employeee.objects.all()
    if query:
        employee=Employeee.objects.filter(
            Q(id__iexact=query) |
            Q(Employeename__icontains=query)
        ) 

    return render(request,'myapp/employee.html',{'emplist':employee})


def register(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emplist')
    return render(request,'myapp/register.html',{'form':form})



def edit(request,id):
    employee=get_object_or_404(Employeee,pk=id)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emplist')
    else:
        form=EmployeeForm(instance=employee)


    return render(request,'myapp/edit.html',{'form':form})


def show(request,id):
    employee=get_object_or_404(Employeee,pk=id)
    return render(request,'myapp/show.html',{'emp':employee})



def delete(request,id):
    employee=get_object_or_404(Employeee,pk=id)
    employee.delete()
    return redirect('emplist')