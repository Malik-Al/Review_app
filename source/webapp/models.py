from django.conf import settings
from django.db import models


CATEGORY_CHOICES = (
    ('other', 'Другое'),
    ('delivery', 'Доставка'),
    ('food', 'Еда'),
    ('clothes', 'Одежда'),
    ('household', 'Товары для дома'),
)


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=300, verbose_name='Описание')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default=CATEGORY_CHOICES[0][0],
                                verbose_name='Категория')
    photo = models.ImageField(upload_to='product_images', null=True, blank=True, verbose_name='Фото')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Feedback(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
                             verbose_name='Автор', related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар', related_name='reviews_products')
    assessment = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name='Оценка')
