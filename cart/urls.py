from django.urls import path

from cart.views import CartView, add_to_cart, minus_quantity, delete_cart_item

urlpatterns = [
    path('', CartView.as_view(), name='cart'),  # Корзина
    path('add_to_cart/<int:id>/', add_to_cart, name='add_to_cart'),  # Добавление в корзину/Увеличение количества в корзине
    path('minus_quantity/<int:id>/', minus_quantity, name='minus_quantity'),  # Уменьшение количества в корзине
    path('delete_cart_item/<int:id>/', delete_cart_item, name='delete_cart_item'),  # Удаление из корзины
]
