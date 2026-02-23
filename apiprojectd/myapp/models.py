from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=60)
    price=models.IntegerField()
    quantity=models.IntegerField()
    image=models.URLField()
    

class Customer(models.Model):
    cname=models.CharField(max_length=60)
    caddress=models.CharField(max_length=60)
    cphone=models.CharField(max_length=12)
    cimage=models.URLField()


class CheckOut(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    created_at=models.DateField()
    price=models.IntegerField()
    quantity=models.IntegerField()


    def __str__(self):
        return f"{self.product.name} - {self.customer.cname}"
