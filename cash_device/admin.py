from django.contrib import admin

from cash_device.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    """Админская панель для модели Item"""
    list_display = ("title", "price")
    search_fields = ("title",)
