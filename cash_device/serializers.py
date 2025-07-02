from rest_framework import serializers


class CashMachineSerializer(serializers.Serializer):
    """ Сериализатор, который принимает список товаров для расчета чека. """
    items:list[int] = serializers.ListField(
        child=serializers.IntegerField(),
        allow_empty=False
    )
