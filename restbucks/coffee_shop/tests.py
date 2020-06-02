from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from coffee_shop.models import Product, OptionName, Option, OptionValue

GET_PRODUCTS_URL = reverse('coffee_shop:menu')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProductTest(TestCase):

    def setUp(self):
        data = {
            "first_name": "Sadegh",
            "last_name": "Azarkaman",
            "email": "test@test.com",
            "password": "testpass"
        }
        self.client = APIClient()
        self.user = create_user(**data)

        self.product = Product.objects.create(name="Latte", price=1000)
        self.product2 = Product.objects.create(name="Latte2", price=1000)
        self.option_name = OptionName.objects.create(name="Milk")
        self.option = Option.objects. \
            create(product=self.product, name=self.option_name)

        self.option_value = OptionValue.objects.create(option=self.option,
                                                       value="skim")

    def test_get_menu(self):
        """test get menu"""
        resp = self.client.get(GET_PRODUCTS_URL)
        print(resp.content)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
