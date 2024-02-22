from django.core.mail import send_mail


def send_email(user_name, user_email):
    send_mail(
        'Cпасибо что выбрали SHAVASHOP!',
        f'{user_name}, cпасибо что выбрали наc!\n'
        'Предлагаем вам совершить заказ! Пройдите по ссылке \n'
        '\nС уважением, команда SHAVASHOP.',
        'django_fitapp@mail.ru',
        [user_email],
        fail_silently=False,
    )
