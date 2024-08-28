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
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.select_related('proxy').prefetch_related('symbols')

class GroupSymbolListView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.select_related('proxy').prefetch_related('symbols')

class PredictionListView(generics.ListAPIView):
    serializer_class = PredictionSerializer

    def get_queryset(self):

        return Prediction.objects.filter(symbol__isnull=False, predicted_class__isnull=False, probability__isnull=False, probabilities__isnull=False, up_date__isnull=False).select_related('symbol')


class UpdateLogView(APIView):

    def post(self, request, *args, **kwargs):
        type = request.data.get('type')
        description = request.data.get('description')
        if type and description:
            Log.objects.create(type=type, description=description)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)

# 'https://chillacoin.ru/f-binance/group/3/?format=json'

# 'https://chillacoin.ru/f-binance/prediction/?format=json'