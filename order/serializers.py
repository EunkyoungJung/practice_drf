from .models import Customer, Order
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    customers = CustomerSerializer(read_only=True, many=True)
    class Meta:
        model=Order
        fields='__all__'



