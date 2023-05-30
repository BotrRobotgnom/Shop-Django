from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity']
    list_filter = ['quantity']

admin.site.register(Product, ProductAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'get_items_display', 'get_total_price')

    def get_items_display(self, obj):
        return ', '.join([f'{product.name}: {quantity}' for product, quantity in self.items.items()])
    get_items_display.short_description = 'Items'

    def get_total_price(self, obj):
        return obj.get_total_price()
    get_total_price.short_description = 'Total Price'

admin.site.register(Order, OrderAdmin)
