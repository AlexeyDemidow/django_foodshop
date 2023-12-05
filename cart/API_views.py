from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from cart.models import CartItem
from cart.serializers import CartSerializer, AllCartSerializer


class AllCartFoodsAPIViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        viewsets.GenericViewSet):

    """Список всех продуктов в корзине у всех"""
    serializer_class = AllCartSerializer
    permission_classes = (IsAuthenticated, IsAdminUser)
    queryset = CartItem.objects.all()


class CartFoodsAPIViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):

    """Список продуктов в корзине у пользователя"""
    serializer_class = CartSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        cart_item = CartItem.objects.filter(user=self.request.user).values(
            'id',
            'product_id',
            'user__customer__customer_name',
            'product__name',
            'quantity',
            'product__price',
        )
        for i in cart_item:
            i['total_price'] = i['quantity'] * i['product__price']
        return cart_item

    @action(detail=False, methods=['get'], url_path=r'cart_price')
    def cart_price(self, request):
        cart_item = self.get_queryset()
        cart_price = 0
        for i in cart_item:
            cart_price += i['total_price']
        return Response({'cart_price': cart_price})

    @action(detail=True, methods=['get'], url_path=r'delete_from_cart')
    def delete_from_cart(self, request, pk):
        cart_item = get_object_or_404(CartItem, id=pk)
        if cart_item:
            cart_item.delete()
        return Response('Товар удален из корзины')

    @action(detail=True, methods=['get'], url_path=r'minus_cart_quantity')
    def minus_cart_quantity(self, request, pk):
        cart_item = get_object_or_404(CartItem, id=pk)
        if cart_item:
            cart_item.quantity -= 1
            cart_item.save()
            if cart_item.quantity <= 0:
                self.delete_from_cart(request=request, pk=pk)
                return Response('Товар удален из корзины')
        return Response('-1')
