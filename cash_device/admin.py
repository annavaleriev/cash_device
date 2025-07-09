from django.contrib import admin

from cash_device.models import Item, Receipt


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Админская панель для модели Item"""
    list_display = ("title", "price")
    search_fields = ("title",)


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    """Админская панель для модели Receipt"""
    list_display = ("file",)
    search_fields = ("file",)
