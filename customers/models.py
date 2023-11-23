from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    """Модель пользователя"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_name = models.CharField(
        null=True,
        blank=True,
        max_length=150,
        help_text='Имя',
    )
    telephone = models.CharField(max_length=100, blank=True, help_text='Телефон')
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        verbose_name='Дата рождения',
        help_text='Введите в формате ДД.ММ.ГГГГ',
    )

    def __str__(self):
        return str(self.user.email)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """Создание/обновление профиля при создании/обновлении аккаунта"""

    if created:
        Customer.objects.create(user=instance)
    instance.customer.save()
