from django.db import models

# Create your models here.
class Product(models.Model):
    ProductId=models.IntegerField()
    ProductName=models.CharField(max_length=100)
    ProductImage=models.URLField(max_length=600)
    ProductPrice=models.IntegerField()
    ProductQuantity=models.IntegerField()

    # def __str__(self):
    #     return self.__str__