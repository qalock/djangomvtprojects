from django.db import models

# Create your models here.

class Employee(models.Model):
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    name=models.CharField(max_length=60)
    salary=models.IntegerField()
    location=models.CharField(max_length=60)
