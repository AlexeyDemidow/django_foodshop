from django.contrib import admin

from cart.models import CartItem


class CartItemAdmin(admin.ModelAdmin):
    """Модель товара в корзине для админ-панели"""

    class Meta:
        model = CartItem

    list_display = ['user', 'product', 'quantity']


admin.site.register(CartItem, CartItemAdmin)
