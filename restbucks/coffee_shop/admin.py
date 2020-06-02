from django.contrib import admin

from coffee_shop.models import Product, \
    Option, OptionName, OptionValue


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


@admin.register(Option)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'name')


@admin.register(OptionName)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(OptionValue)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('option', 'value')
