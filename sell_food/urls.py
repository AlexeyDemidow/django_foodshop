from django.urls import path

from sell_food.views import FoodPageView, FoodCatalogView, food_search

urlpatterns = [
    path('<int:pk>/', FoodPageView.as_view(), name='foodpage'),  # Страница товара
    path('', FoodCatalogView.as_view(), name='catalog'),  # Каталог
    path('food_search/', food_search, name='food_search'),  # Поиск товаров

]
