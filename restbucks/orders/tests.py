from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from coffee_shop.models import Product, OptionName, Option, OptionValue
from orders.models import Order

ORDER_URL = reverse('order-list')


def get_detail_url(order_id):
    """get url of product id"""
    return reverse("order-detail", args=[str(order_id)])


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class ProductTest(TestCase):

    def setUp(self):
        user_obj = {
            "first_name": "Sadegh",
            "last_name": "Azarkaman",
            "email": "test@test.com",
            "password": "testpass",
            "role": get_user_model().MANAGER
        }
        self.client = APIClient()
        self.user = create_user(**user_obj)
        self.product = Product.objects.create(name="Latte", price=1000)
        self.option_name = OptionName.objects.create(name="Milk")
        self.option = Option.objects.create(product=self.product,
                                            name=self.option_name)

        self.option_value = OptionValue.objects.create(option=self.option,
                                                       value="skim")

        self.order = Order.objects.create(product=self.product,
                                          count=1,
                                          option_value=self.option_value)

    def test_order_product(self):
        """test if user can order a product"""
        self.client.force_authenticate(self.user)
        resp = self.client.post(ORDER_URL, data={
            "product": self.product.id,
            "count": 1,
            "option_value": self.option_value.id
        })
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

    def test_get_order(self):
        """test of customer can get his order"""
        self.client.force_authenticate(self.user)
        url = get_detail_url(self.order.id)
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        with self.subTest('Unauthenticated users may not use the API.'):
            self.client.logout()
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_manager_change_order_status(self):
        """manager can change order status"""
        self.client.force_authenticate(self.user)
        cancel = "CA"
        url = reverse('order-set_status', args=[self.order.id])
        resp = self.client.patch(url, data={
            "status": cancel
        })
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        new_status = Order.objects.values("status").get(pk=self.order.id)
        self.assertEqual(new_status["status"],  cancel)

        with self.subTest('customer can not change order status'):
            self.user.role = get_user_model().CUSTOMER
            self.client.force_authenticate(self.user)
            resp = self.client.patch(url, data={
                "status": cancel
            })
            self.assertEqual(resp.status_code, status.HTTP_403_FORBIDDEN)
