from django.contrib.auth.models import User
from rest_framework import serializers

from cart.models import CartItem
from sell_food.models import Food


class FoodsSerializer(serializers.ModelSerializer):
    """Все продукты"""

    class Meta:
        model = Food
        fields = '__all__'
