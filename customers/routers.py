from rest_framework import routers

from .API_views import AllCustomersAPIViewSet, AllUsersAPIViewSet, AllProfileAPIViewSet, ProfileAPIViewSet, \
    UserAPIViewSet

# Роутер взаимодействия админа с профилями пользователей
admin_all_customers_router = routers.SimpleRouter()
admin_all_customers_router.register(r'admin_all_customers', AllCustomersAPIViewSet)

admin_users_edit_router = routers.SimpleRouter()
admin_users_edit_router.register(r'admin_users_edit', AllUsersAPIViewSet)

admin_customers_edit_router = routers.SimpleRouter()
admin_customers_edit_router.register(r'admin_customers_edit', AllProfileAPIViewSet)

customer_profile_router = routers.SimpleRouter()
customer_profile_router.register(r'customer_profile', ProfileAPIViewSet, basename='customer_profile')

customer_account_router = routers.SimpleRouter()
customer_account_router.register(r'customer_account', UserAPIViewSet, basename='customer_account')
