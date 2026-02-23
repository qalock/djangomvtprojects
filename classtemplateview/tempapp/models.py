from django.db import models

# Create your models here.
class Student(models.Model):
    StudentId=models.IntegerField()
    StudentName=models.CharField(max_length=60)
    StudentFees=models.IntegerField()
    