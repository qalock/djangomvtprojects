from django.shortcuts import render
from .models import Product,Customer,CheckOut
from .serializers import ProductSerializer,CustomerSerializer,OrderSerializer
from rest_framework import viewsets

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset=CheckOut.objects.all()
    serializer_class=OrderSerializer
