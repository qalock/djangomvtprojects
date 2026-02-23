from django.shortcuts import render,redirect
from .models import Employees
from django.contrib import messages
from .forms import EmployeeForm


# Create your views here.
def register(request):
    form=EmployeeForm()
    if request.method=="POST":
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request,'Data Added Successfully!!')
            return redirect('add')
    return render(request,'myapp/reqister.html',{'form':form})