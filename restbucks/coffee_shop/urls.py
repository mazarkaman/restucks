from django.urls import path

from coffee_shop.views import MenuView

app_name = 'coffee_shop'

urlpatterns = [
    path('menu/', MenuView.as_view(), name='menu'),
]
