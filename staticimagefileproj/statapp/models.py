from django.db import models

# Create your models here.
class Statproj(models.Model):
    title=models.CharField(max_length=25)
    image=models.ImageField(upload_to='static\images')