from django.db.models import Prefetch, Max
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Group, Symbol, Log, Prediction
from .serializers import GroupSerializer, SymbolSerializer, PredictionSerializer


class GroupSymbolDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.select_related('proxy').prefetch_related('symbols')

class SymbolDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Symbol.objects.all()
    serializer_class = SymbolSerializer
class GroupSymbolListView(generics.ListAPIView):
    serializer_class = GroupSerializer

    def get_queryset(self):
        return Group.objects.select_related('proxy').prefetch_related('symbols')

class UpdateLogView(APIView):

    def post(self, request, *args, **kwargs):
        type = request.data.get('type')
        description = request.data.get('description')
        if type and description:
            Log.objects.create(type=type, description=description)
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class PredictionListView(generics.ListAPIView):
    serializer_class = PredictionSerializer

    def get_queryset(self):
        return Prediction.objects.filter(symbol__isnull=False, predicted_class__isnull=False, probability__isnull=False,
                                         probabilities__isnull=False, up_date__isnull=False).select_related(
            'symbol')
