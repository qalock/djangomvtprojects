from django.db import models

# Create your models here.
class Products(models.Model):
    product_id=models.IntegerField()
    product_name=models.CharField(max_length=15)
    product_price=models.IntegerField()
    product_quant=models.IntegerField()