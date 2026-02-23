from django.contrib import admin
from .models import Product,Customer,CheckOut


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','quantity','image']

class CustomerAdmin(admin.ModelAdmin):
    list_display=['id','cname','caddress','cphone','cimage']

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','product','customer','created_at','price','quantity']


admin.site.register(Product,ProductAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(CheckOut,OrderAdmin)