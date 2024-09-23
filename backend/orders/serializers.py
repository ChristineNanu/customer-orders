from rest_framework import serializers
from .models import Order
from customers.models import Customer


class OrderSerializer(serializers.ModelSerializer):
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())

    class Meta:
        model = Order
        fields = ["id", "customer", "item", "amount", "time"]
