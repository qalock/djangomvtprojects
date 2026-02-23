from django import forms
from .models import Employees

class EmployeeForm(forms.ModelForm):
    employee_name=forms.CharField(max_length=60)
    employee_job=forms.CharField(max_length=60)
    employee_age=forms.IntegerField()
    employee_loc=forms.CharField(max_length=60)

    class Meta:
        model=Employees
        fields='__all__'