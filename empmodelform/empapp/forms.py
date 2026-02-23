from django import forms
from empapp.models import Employee

class EmployeeForm(forms.ModelForm):
    EmployeeID=forms.IntegerField()
    EmployeeName=forms.CharField(max_length=60)
    EmployeeSalary=forms.IntegerField()
    EmployeeDept=forms.CharField(max_length=60)


    class Meta:
        model=Employee
        fields="__all__"