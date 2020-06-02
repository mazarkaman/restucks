from django.db import models
from coffee_shop.models import Product, Option, OptionValue
from django.contrib.auth import get_user_model


class Order(models.Model):
    """model for user orders"""

    WAITING = 'WA'
    PREPARE = 'PR'
    READY = 'RE'
    DELIVER = 'DE'
    CANCELED = 'CA'
    ORDER_STATUS_CHOICES = [
        (WAITING, 'Waiting'),
        (PREPARE, 'Prepare'),
        (READY, 'Ready'),
        (DELIVER, 'Deliver'),
        (CANCELED, 'Canceled'),
    ]

    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
    )
    option_value = models.ForeignKey(
        to=OptionValue,
        on_delete=models.CASCADE,
    )
    count = models.IntegerField(null=False)
    status = models.CharField(
        max_length=2,
        choices=ORDER_STATUS_CHOICES,
        default=WAITING,
    )
