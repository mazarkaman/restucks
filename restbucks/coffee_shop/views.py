from rest_framework import generics
from rest_framework.permissions import AllowAny

from coffee_shop.models import OptionValue, Product
from coffee_shop.serializers import  ProductSerializer


class MenuView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
