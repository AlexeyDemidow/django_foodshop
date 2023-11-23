from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from cart.models import CartItem
from sell_food.models import Food


class CartView(LoginRequiredMixin, ListView):
    """Представление списка товаров в корзине"""

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)

    def sum_price(self):
        """Подсчет итоговой стоимости всех товаров в корзине"""

        food_object = CartItem.objects.filter(user=self.request.user)
        total = 0
        for item in food_object:
            total += item.total_price()
        return total

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sum_price'] = self.sum_price()
        return context

    context_object_name = 'cart_item'
    template_name = 'cart.html'


@login_required
def add_to_cart(request, id):
    """Представление для AJAX-запроса добавления товара в корзину и увеличения количества в корзине"""

    product = get_object_or_404(Food, id=id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if cart_item:
        cart_item.quantity += 1
        cart_item.save()

    return JsonResponse({'status': 'success'})


@login_required
def minus_quantity(request, id):
    """Представление для AJAX-запросов уменьшения количества товаров в корзине"""

    product = get_object_or_404(Food, id=id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

    if cart_item:
        if cart_item.quantity >= 2:
            cart_item.quantity -= 1
            cart_item.save()
        else:
            cart_item.quantity = 1
            cart_item.save()

    return JsonResponse({'status': 'success'})


@login_required
def delete_cart_item(request, id):
    """Представление для AJAX-запроса на удаление товара из корзины"""

    item = get_object_or_404(CartItem, id=id)
    item.delete()
    return JsonResponse({'status': 'success'})
