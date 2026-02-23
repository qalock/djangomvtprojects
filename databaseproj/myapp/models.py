from django.db import models

# Create your models here.
class Employeee(models.Model):
    Employeename=models.CharField(max_length=60)
    Employeesalary=models.IntegerField()
    Employeedept=models.CharField(max_length=60)