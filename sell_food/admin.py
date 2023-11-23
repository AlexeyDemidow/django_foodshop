from django.contrib import admin

from .models import *


class FoodAdmin(admin.ModelAdmin):
    """Модель товара в админ-панели"""

    class Meta:
        model = Food

    list_display = ['name', 'description', 'weight', 'price']


admin.site.register(Food, FoodAdmin)
