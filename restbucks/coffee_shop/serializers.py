from rest_framework import serializers

from coffee_shop.models import Product, OptionValue, Option, OptionName


class ProductSerializer(serializers.ModelSerializer):
    """serializer for product"""
    class Meta:
        model = Product
        fields = '__all__'


class OptionValueSerializer(serializers.ModelSerializer):
    """serializer for option value"""
    class Meta:
        model = OptionValue
        fields = '__all__'


class OptionSerializer(serializers.ModelSerializer):
    """serializer for option"""
    class Meta:
        model = Option
        fields = '__all__'


class OptionNameSerializer(serializers.ModelSerializer):
    """serializer fot option name"""
    class Meta:
        model = OptionName
        fields = '__all__'


class OptionDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    name = OptionNameSerializer()

    class Meta:
        model = Option
        fields = '__all__'





