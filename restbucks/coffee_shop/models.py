from django.db import models


class Product(models.Model):
    """model for product"""
    name = models.CharField(max_length=50)
    price = models.IntegerField(null=False)


class Option(models.Model):
    """model for product options"""
    product = models.ForeignKey(
        "product",
        on_delete=models.CASCADE,
    )
    name = models.ForeignKey(
        "OptionName",
        on_delete=models.CASCADE,
    )


class OptionName(models.Model):
    """model for option name for ex:size,shot,kind"""
    name = models.CharField(max_length=50)


class OptionValue(models.Model):
    """model for value of each option for ex: skim, semi, whole """
    option = models.ForeignKey(
        "Option",
        on_delete=models.CASCADE,
    )
    value = models.CharField(max_length=50)
