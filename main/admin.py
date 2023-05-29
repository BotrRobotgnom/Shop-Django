from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    list_filter = ['quantity']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'status']
    list_filter = ['status']

admin.site.register(Order, OrderAdmin)