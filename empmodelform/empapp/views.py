from django.shortcuts import render ,redirect,get_object_or_404
from django.db.models import Q
from empapp.forms import EmployeeForm
from empapp.models import Employee
# Create your views here.

def employee(request):
    query=request.GET.get('q')
    Employees=Employee.objects.all()
    if query:
        Employees=Employee.objects.filter(
            Q(EmployeeID__iexact=query) |
            Q(EmployeeName__icontains=query)
        )
    return render(request,'empapp/employee.html',{'emplist':Employees})


def register(request):
    form=EmployeeForm()
    if request.method== 'POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('emplist')

    return render(request,'empapp/register.html',{'form':form})

def edit(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    if request.method=="POST":
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
            return redirect('emplist')
    else:
        form=EmployeeForm(instance=employee)
    return render(request,'empapp/edit.html',{'form':form})

def show(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    return render(request,'empapp/show.html',{'employee':employee})


def delete(request,pk):
    employee=get_object_or_404(Employee,pk=pk)
    employee.delete()
    return redirect('emplist')
