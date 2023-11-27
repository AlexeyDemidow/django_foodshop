from rest_framework import routers

from sell_food.API_views import AllFoodsAPIViewSet

all_foods_router = routers.SimpleRouter()
all_foods_router.register(r'all_foods', AllFoodsAPIViewSet)
