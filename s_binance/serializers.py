from rest_framework import serializers
from .models import Symbol, Group, Proxy


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