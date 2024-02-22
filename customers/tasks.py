from django.core.mail import send_mail
from django_foodshop.celery import app
from .service import send_email
from .models import Customer


@app.task
def send_mailing(user_name, user_email):
    send_email(user_name, user_email)


@app.task
def beat_mailing():
    for user in Customer.objects.all():
        if user.customer_name is not None:
            send_mail(
                'SHAVASHOP',
                f'{user.customer_name}, вам, как нашему любимому клиенту предоставлена скидка 5%!.\n'
                'Предлагаем вам сделать заказ в SHAVASHOP!',
                'django_fitapp@mail.ru',
                [user.user.email],
                fail_silently=False,
            )
        else:
            send_mail(
                'SHAVASHOP',
                f'{user.user.username}, вам, как нашему любимому клиенту предоставлена скидка 5%!.\n'
                'Предлагаем вам сделать заказ в SHAVASHOP!',
                'django_fitapp@mail.ru',
                [user.user.email],
                fail_silently=False,
            )