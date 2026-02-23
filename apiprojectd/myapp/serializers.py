from .models import Product,Customer,CheckOut
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model=Product
        fields='__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    customer_name = serializers.CharField(source='customer.cname', read_only=True)

    class Meta:
        model=CheckOut
        fields='__all__'