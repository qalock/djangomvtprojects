from django.shortcuts import render
from django.views.generic import *
from .models import Employee
from django.urls import reverse_lazy


# Create your views here.
class Employees(ListView):
    model=Employee
    
    

class AddEmployee(CreateView):
    model=Employee
    fields='__all__'
    

class EditEmployee(UpdateView):
    model=Employee
    fields=['EmpId','EmpName','EmpSal']

class DeleteEmployee(DeleteView):
    model=Employee
    success_url=reverse_lazy('list')

class FindEmployee(DetailView):
    model=Employee
