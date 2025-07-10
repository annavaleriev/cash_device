from rest_framework import serializers

from cash_device.models import Item


class CashMachineSerializer(serializers.Serializer):
    """Сериализатор для кассового аппарата"""

    items = serializers.PrimaryKeyRelatedField(queryset=Item.objects.all(), many=True)


# Этот сериализатор проверяет входные данные: список ID товаров, которые передаёт пользователь.
#
# Пример запроса:
#
# json
# Копировать
# Редактировать
# {
#   "items": [1, 2, 3]
# }

# наверное нужен сериаолизатор для чека, но пока не реализован.
