from django.contrib.auth.models import User
from django.db import models

from sell_food.models import Food


class CartItem(models.Model):
    """Модель товара в корзине"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def total_price(self):
        """Подсчет итоговой цены в зависимости от цены за один предмет и количество"""
        return self.product.price * self.quantity
