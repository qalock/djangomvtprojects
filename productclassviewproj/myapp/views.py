from django.shortcuts import render
from django.views.generic import *
from django.urls import reverse_lazy
from .models import Product

# Create your views here.

class Products(ListView):
    model=Product

class AddProduct(CreateView):
    model=Product
    fields='__all__'

class EditProduct(UpdateView):
    model=Product
    fields=['ProductName','ProdcutImage','ProductPrice','ProductQuant']

class DeleteProduct(DeleteView):
    model=Product 
    success_url=reverse_lazy('list')

class ShowProduct(DetailView):
    model=Product