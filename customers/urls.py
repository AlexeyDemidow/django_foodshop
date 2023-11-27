from django.urls import path

from customers.views import SignUpView, SignUpSuccess, Login, Profile, UpdateProfile
from django.contrib.auth import views

urlpatterns = [
    path('<int:pk>/', Profile.as_view(), name='customer_profile'),  # Профиль
    path('<int:pk>/edit_profile/', UpdateProfile.as_view(), name='edit_profile'),  # Обновление данных профиля
    path('signup/', SignUpView.as_view(), name='signup'),  # Регистрация
    path('signup_success/', SignUpSuccess.as_view(), name='signup_success'),  # Сигнал об успешной регистрации
    path('login/', Login.as_view(), name='user_login'),  # Вход
    path('logout/', views.LogoutView.as_view(), name='user_logout'),  # Выход
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),  # Сброс пароля
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Сигнал об успешном сбросе пароля
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Подтверждение сброса пароля
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Сброс пароля успешен

]
