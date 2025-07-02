from django.db import models


class Item(models.Model):
    """Модель для товаров в магазине"""
    title = models.CharField(max_length=200, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title
