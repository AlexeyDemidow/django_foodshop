from django.db import models
from PIL import Image


class Food(models.Model):
    """Модель товара"""

    name = models.CharField(max_length=100, verbose_name='Название продукта')
    description = models.CharField(max_length=500, verbose_name='Описание продукта')
    pic = models.ImageField(default='default.png', upload_to='images/', verbose_name='Изображение',)

    weights = [300, 450, 700]
    weight_list = [(300, weights[0]), (450, weights[1]), (700, weights[2])]
    weight = models.IntegerField(choices=weight_list, default=weights[0], verbose_name='Вес')

    price = models.DecimalField(max_digits=5, decimal_places=2, default=1.5, blank=True, verbose_name='Цена')

    def save(self, *args, **kwargs):
        # Если цена задана вручную, то сохраняем ее без вычисления новой цены
        if self.price:
            super().save(*args, **kwargs)
        else:
            # Вычисляем новую цену на основе выбранного веса
            self.price = self.weight * 1.5 / 100
            super().save(*args, **kwargs)

        if not self.pic:
            self.pic = 'default.png'
        img = Image.open(self.pic.path)
        if img.height > 400 or img.width > 400:
            output_size = (400, 400)
            img.thumbnail(output_size)
            img.save(self.pic.path)

    def __str__(self):
        return str(self.name)
