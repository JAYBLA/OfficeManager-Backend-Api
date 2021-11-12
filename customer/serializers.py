from rest_framework import serializers 
from customer.models import Customer
 
 
class CustomerSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'physical_address',]