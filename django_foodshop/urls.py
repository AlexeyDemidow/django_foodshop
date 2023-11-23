from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),  # Админ-панель
    path('food_catalog/', include('sell_food.urls')),  # Каталог товаров
    path('customers/', include('customers.urls')),  # Страница пользователя
    path('cart/', include('cart.urls')),  # Корзина
    path('', RedirectView.as_view(url='food_catalog/', permanent=True), name='home'),  # Главная

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
