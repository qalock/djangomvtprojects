from django.db import models
from django.urls import reverse


# Create your models here.
class Employee(models.Model):
    EmpId=models.IntegerField()
    EmpName=models.CharField(max_length=60)
    EmpSal=models.IntegerField()
    

    def get_absolute_url(self):
        return reverse('list')