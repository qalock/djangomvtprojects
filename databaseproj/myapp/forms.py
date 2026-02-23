from django import forms
from .models import Employeee

class EmployeeForm(forms.ModelForm):


    class Meta:
        model=Employeee
        fields=["Employeename","Employeesalary","Employeedept"]