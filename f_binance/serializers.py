from rest_framework import serializers
from .models import Symbol, Filter, Group


class FilterSerializer(serializers.ModelSerializer):
    class Meta:
       model = Filter
       fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Удаляем пустые поля из представления
        return {key: value for key, value in representation.items() if value is not None}

class SymbolSerializer(serializers.ModelSerializer):
    filters = FilterSerializer(many=True, read_only=True)
    class Meta:
       model = Symbol
       fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    symbols = SymbolSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = '__all__'