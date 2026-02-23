from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    ProductId=models.IntegerField()
    ProductName=models.CharField(max_length=60)
    ProdcutImage=models.URLField(max_length=255)
    ProductPrice=models.IntegerField()
    ProductQuant=models.IntegerField()

    def get_absolute_url(self,):
        return reverse('list')

    