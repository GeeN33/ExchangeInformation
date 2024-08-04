from datetime import timedelta
from django.utils import timezone
from django.db.models import Prefetch, Max
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Symbol, Group, Log, Prediction
from .serializers import SymbolSerializer, GroupSerializer, PredictionSerializer


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

class PredictionListView(generics.ListAPIView):
    serializer_class = PredictionSerializer

    def get_queryset(self):

        return Prediction.objects.select_related('symbol').all()


class UpdateLogView(APIView):

    def post(self, request, *args, **kwargs):
        type = request.data.get('type')
        description = request.data.get('description')
        if type and description:
            Log.objects.create(type=type, description=description)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

# 'https://chillacoin.ru/f-binance/group/3/?format=json'

# 'https://chillacoin.ru/f-binance/prediction/?format=json'