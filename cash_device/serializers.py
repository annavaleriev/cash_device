from rest_framework import serializers

from cash_device.models import Item

class CashMachineSerializer(serializers.Serializer):
    """ Сериализатор для кассового аппарата """
    items = serializers.PrimaryKeyRelatedField(
        queryset=Item.objects.all(),
        many=True
    )
