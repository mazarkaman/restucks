from rest_framework import serializers

from coffee_shop.serializers import ProductSerializer, OptionValueSerializer
from orders.models import Order


class OrderSerializer(serializers.ModelSerializer):
    """serializer of order"""
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    option_value = OptionValueSerializer()

    class Meta:
        model = Order
        fields = '__all__'
