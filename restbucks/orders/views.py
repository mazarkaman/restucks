from django.shortcuts import render
from rest_framework import mixins, authentication, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from orders.models import Order
from orders.serializers import OrderSerializer, OrderDetailSerializer
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model


class IsManagerPermission(permissions.BasePermission):
    """
    also can be implemented using [IsAdminUser] permission but i created this
    for testing
    """

    def has_permission(self, request, view):
        return request.user.role == get_user_model().MANAGER


class OrderViewSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def retrieve(self, request, *args, **kwargs):
        order_details = self.get_object()
        serializer = OrderDetailSerializer(instance=order_details)
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], url_name='set_status',
            permission_classes=[IsManagerPermission]
            )
    def set_status(self, request, pk=None):
        """change status of order"""
        order = self.get_object()
        st = request.data.get("status")
        try:
            if st:
                order.status = st
                order.save()
                return Response(_("status set"))
            return Response(_("status parameter not provided"),
                            status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(ex, status=status.HTTP_400_BAD_REQUEST)
