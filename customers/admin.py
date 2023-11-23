from django.contrib import admin

from .models import *


class CustomerAdmin(admin.ModelAdmin):
    """Модель пользователя в админ-панели"""

    class Meta:
        model = Customer

    list_display = ['user', 'customer_name', 'date_of_birth', 'telephone']


admin.site.register(Customer, CustomerAdmin)
