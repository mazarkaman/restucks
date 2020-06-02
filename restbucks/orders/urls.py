from django.urls import path
from django.urls.conf import include, re_path
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet


router = DefaultRouter()
router.register("", OrderViewSet, basename='order')

urlpatterns = [
    re_path('^', include(router.urls)),
]
