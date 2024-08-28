from rest_framework import serializers

from .models import Symbol, SubGroup, Group, Prediction


class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Symbol
        fields = ('symbol','status',)

class SubGroupSerializer(serializers.ModelSerializer):

    symbols = SymbolSerializer(many=True, read_only=True)
    class Meta:
        model = SubGroup
        fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):

    subgroup = SubGroupSerializer(many=True, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prediction
        fields = '__all__'
