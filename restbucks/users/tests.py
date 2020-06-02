from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('users:create')
LOGIN_USER_URL = reverse('users:token')


def creat_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUsersApiTest(TestCase):
    """Tests users api"""
    F_NAME = "Sadegh"
    L_NAME = "Azarkaman"
    EMAIL = "azarkaman.net@gmail.com"
    PASS = "1234"

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):
        """test if user create successfully"""
        response = self.client.post(CREATE_USER_URL, data={
            "first_name": self.F_NAME,
            "last_name": self.L_NAME,
            "email": self.EMAIL,
            "password": self.PASS
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**response.data)
        self.assertTrue(user.check_password(self.PASS))
        self.assertNotIn('password', response.data)

    def test_login_api_success(self):
        """test if user login success"""
        data = {
            "first_name": self.F_NAME,
            "last_name": self.L_NAME,
            "email": self.EMAIL,
            "password": self.PASS
        }
        creat_user(**data)
        response = self.client.post(LOGIN_USER_URL,
                                    {"email": self.EMAIL,
                                     "password": self.PASS})
        self.assertIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_api_fail(self):
        """test if login fails"""
        data = {
            "first_name": self.F_NAME,
            "last_name": self.L_NAME,
            "email": self.EMAIL,
            "password": self.PASS
        }
        creat_user(**data)
        self.client.post(LOGIN_USER_URL)
        response = self.client.post(LOGIN_USER_URL,
                                    {"email": self.EMAIL,
                                     "password": "wrong"})
        self.assertNotIn("token", response.data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
