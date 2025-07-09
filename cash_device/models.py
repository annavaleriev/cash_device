from django.db import models


class Item(models.Model):
    """Модель для товаров в магазине"""
    title = models.CharField(max_length=200, verbose_name="Название")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Receipt(models.Model):
    """Модель для чеков"""
    file = models.FileField(verbose_name="Чек", upload_to="cash_device")

    def __str__(self):
        return str(self.file.name)

    class Meta:
        verbose_name = "Чек"
        verbose_name_plural = "Чеки"
