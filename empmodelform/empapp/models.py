from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeID=models.IntegerField()
    EmployeeName=models.CharField(max_length=60)
    EmployeeSalary=models.IntegerField()
    EmployeeDept=models.CharField(max_length=60)