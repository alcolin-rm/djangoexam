from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(AbstractUser):
    bonus_balance = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name='Баланс бонусов'
    )

    def __str__(self):
        return self.username


class Dish(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость'
    )
    image = models.ImageField(
        upload_to='dishes/',
        verbose_name='Фотография'
    )

    def __str__(self):
        return self.name


class Order(models.Model):
    client = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Клиент'
    )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Блюдо'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.client.username} — {self.dish.name}'