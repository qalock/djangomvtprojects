from django.shortcuts import render
from django.views.generic import *
from .models import Student
from django.urls import reverse_lazy

# Create your views here.

class Students(ListView):
    model=Student

class AddStudent(CreateView):
    model=Student
    fields='__all__'

class EditStudent(UpdateView):
    model=Student
    fields=['StudentName','StudentMarks']

class DetailStudent(DetailView):
    model=Student

class DeleteStudent(DeleteView):
    model=Student
    fields='__all__'

    success_url= reverse_lazy('list')