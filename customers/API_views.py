from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from customers.models import Customer
from customers.serializers import CustomerSerializer, UserSerializer, ProfileSerializer


class AllCustomersAPIViewSet(mixins.ListModelMixin,
                             mixins.RetrieveModelMixin,
                             viewsets.GenericViewSet):
    """Общий вид профилей всех пользователей"""
    queryset = Customer.objects.values(
        'id',
        'user__username',
        'user__email',
        'customer_name',
        'date_of_birth',
        'telephone'
    )

    serializer_class = CustomerSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class AllUsersAPIViewSet(viewsets.ModelViewSet):
    """Список всех пользователей и их редактирование"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class AllProfileAPIViewSet(viewsets.ModelViewSet):
    """Список всех профилей пользователей и их редактирование"""

    queryset = Customer.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAdminUser, IsAuthenticated)


class ProfileAPIViewSet(mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        viewsets.GenericViewSet):
    """Профиль пользователя и их изменение"""

    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        customer = self.request.user.customer.id
        user_profile = Customer.objects.filter(id=customer)
        return user_profile


class UserAPIViewSet(mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     viewsets.GenericViewSet):
    """Данные пользователя и их изменение"""
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user.id
        user_acc = User.objects.filter(id=user)
        return user_acc
