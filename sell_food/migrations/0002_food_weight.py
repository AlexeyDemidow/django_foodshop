# Generated by Django 4.2.7 on 2023-11-03 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sell_food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='weight',
            field=models.IntegerField(choices=[(300, 300), (450, 450), (700, 700)], default=300, verbose_name='Вес'),
        ),
    ]
