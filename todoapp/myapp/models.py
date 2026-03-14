from django.db import models

# Create your models here.

class Data(models.Model):
    head=models.CharField(max_length=150)
    des=models.TextField()
    time=models.DateTimeField(auto_now_add=True)
