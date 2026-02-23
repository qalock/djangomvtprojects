from django.db import models

# Create your models here.


class Employees(models.Model):
    employee_name=models.CharField(max_length=60)
    employee_job=models.CharField(max_length=60)
    employee_age=models.IntegerField()
    employee_loc=models.CharField(max_length=60)

   