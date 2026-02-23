from django.db import models

# Create your models here.
class Otp(models.Model):
    email=models.EmailField()
    otp=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)


    