from django.db import models
from django.urls import reverse

# Create your models here.
class Student(models.Model):
    StudentId=models.IntegerField()
    StudentName=models.CharField(max_length=40)
    StudentMarks=models.IntegerField()

    def get_absolute_url(self):
        return reverse('list')