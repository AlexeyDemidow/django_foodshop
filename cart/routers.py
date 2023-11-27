from rest_framework import routers

from cart.API_views import CartFoodsAPIViewSet, AllCartFoodsAPIViewSet

cart_router = routers.SimpleRouter()
cart_router.register(r'cart_foods', CartFoodsAPIViewSet, basename='cart_foods')

all_cart_router = routers.SimpleRouter()
all_cart_router.register(r'all_cart_foods', AllCartFoodsAPIViewSet, basename='all_cart_foods')
