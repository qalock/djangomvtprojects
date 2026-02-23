from django.db import models

# Create your models here.
class Product(models.Model):
    productname=models.CharField(max_length=60)
    productimage=models.ImageField(upload_to='images')
    productprice=models.IntegerField()
    productquantity=models.IntegerField()