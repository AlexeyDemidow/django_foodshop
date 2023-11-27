from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from cart.routers import cart_router, all_cart_router
from customers.routers import admin_users_edit_router, admin_all_customers_router, admin_customers_edit_router, \
    customer_profile_router, customer_account_router
from sell_food.routers import all_foods_router

urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('food_catalog/', include('sell_food.urls')),  # Каталог товаров
    path('customers/', include('customers.urls')),  # Страница пользователя
    path('cart/', include('cart.urls')),  # Корзина
    path('', RedirectView.as_view(url='food_catalog/', permanent=True), name='home'),  # Главная

    path('api/api-auth/', include('rest_framework.urls')),  # Авторизация на основе сессий cookies
    path('api/auth/', include('djoser.urls')),  # Авторизация djoser
    path('api/auth/', include('djoser.urls.authtoken')),  # Авторизация djoser
    path('api/auth/', include('djoser.urls.jwt')),  # Авторизация djoser
    # customers
    path('api/', include(admin_all_customers_router.urls)),  # api/admin_all_customers/{int:id} Просмотр всех профилей пользователя
    path('api/', include(admin_customers_edit_router.urls)),  # api/admin_users_edit/{int:id} Редактирование профилей
    path('api/', include(admin_users_edit_router.urls)),  # api/admin_customers_edit/{int:id} Редактирование пользователей
    path('api/', include(customer_profile_router.urls)),  # /api/customer_profile/{int:id} Профиль
    path('api/', include(customer_account_router.urls)),  # /api/customer_account/{int:id}/ Данные пользователя
    # sell_food
    path('api/', include(all_foods_router.urls)),  # Список всех продуктов и добавление в корзину
    # cart
    path('api/', include(cart_router.urls)),  # /api/all_cart_foods/{int:id} Все продукты в корзине для админов
    path('api/', include(all_cart_router.urls)),  # /api/cart_foods/{int:id} Работа с корзиной, отнять один товар и удалить

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
