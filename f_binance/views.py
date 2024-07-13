from django.db.models import Prefetch
from rest_framework import generics
from .models import Symbol, Group
from .serializers import SymbolSerializer, GroupSerializer


class SymbolListView(generics.ListAPIView):
    queryset = Symbol.objects.prefetch_related('filters')
    serializer_class = SymbolSerializer

class SymbolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer

class GroupSymbolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class GroupSymbolListView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.prefetch_related(
            Prefetch('symbols', queryset=Symbol.objects.prefetch_related('filters'))
        )