from django.contrib import admin
from .models import Products

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','product_price','product_quant']

    class Meta:
        model=Products
        fields='__all__'

admin.site.register(Products,ProductAdmin)