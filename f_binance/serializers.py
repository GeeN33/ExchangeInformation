from rest_framework import serializers
from .models import Symbol, Group, Proxy, Prediction


class ProxySerializer(serializers.ModelSerializer):
    class Meta:
       model = Proxy
       fields = '__all__'

class SymbolSerializer(serializers.ModelSerializer):
    class Meta:
       model = Symbol
       fields = '__all__'

class GroupSerializer(serializers.ModelSerializer):
    symbols = SymbolSerializer(many=True, read_only=True)
    proxy = ProxySerializer(many=False, read_only=True)
    class Meta:
        model = Group
        fields = '__all__'




class PredictionSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    class Meta:
       model = Prediction
       fields = ('name', 'predicted_class', 'probability', 'probabilities', 'up_date')

    def get_name(self, obj):
        return obj.symbol.symbol

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['name'] = self.get_name(instance)
        return ret