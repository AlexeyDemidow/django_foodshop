from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    """Общий вид профилей пользователей"""

    username = serializers.CharField(source='user__username')
    email = serializers.EmailField(source='user__email')

    class Meta:
        model = Customer
        fields = ('id', 'username', 'email', 'customer_name', 'date_of_birth', 'telephone')


class UserSerializer(serializers.ModelSerializer):
    """Список всех пользователей и их редактирование"""

    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class ProfileSerializer(serializers.ModelSerializer):
    """Профилей пользователя и его редактирование"""

    class Meta:
        model = Customer
        fields = ('id', 'customer_name', 'date_of_birth', 'telephone')

