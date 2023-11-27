from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from cart.models import CartItem
from sell_food.models import Food
from sell_food.serializers import FoodsSerializer


class AllFoodsAPIViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """Список всех продуктов"""
    serializer_class = FoodsSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Food.objects.all()

    @action(detail=True, methods=['get'], url_path=r'add_to_cart')
    def add_to_cart(self, request, pk):
        product = get_object_or_404(Food, id=pk)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)

        if cart_item:
            cart_item.quantity += 1
            cart_item.save()
            return Response({'in_cart': 'True'})
        else:
            return Response({'in_cart': 'False'})
