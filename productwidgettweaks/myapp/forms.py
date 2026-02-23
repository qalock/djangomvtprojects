from django import forms
from .models import Products

class ProductForm(forms.ModelForm):


    class Meta:
        model=Products
        fields=['product_id','product_name','product_price','product_quant']