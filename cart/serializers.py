from django.contrib.auth.models import User
from rest_framework import serializers

from cart.models import CartItem


class CartSerializer(serializers.ModelSerializer):
    """Продукты в корзине у пользователя"""

    customer_name = serializers.CharField(source='user__customer__customer_name')
    product_name = serializers.CharField(source='product__name')
    product_price = serializers.DecimalField(max_digits=4, decimal_places=2, source='product__price')

    class Meta:
        model = CartItem
        fields = ('id', 'customer_name', 'product_name', 'quantity', 'product_price', 'total_price')


class AllCartSerializer(serializers.ModelSerializer):
    """Все продукты в корзине"""

    class Meta:
        model = CartItem
        fields = '__all__'