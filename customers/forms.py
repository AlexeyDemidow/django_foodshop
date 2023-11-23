from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


class CustomerCreationForm(UserCreationForm):
    """Форма создания пользователя"""

    class Meta:
        model = User
        fields = ['username', 'email']


class CustomerUpdateForm(UserChangeForm):
    """Форма обновления данных пользователя"""

    password = None

    class Meta:
        model = User
        fields = ['first_name', 'email']


