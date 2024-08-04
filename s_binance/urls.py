from django.urls import path

from .views import SymbolDetailView, GroupSymbolDetailView, GroupSymbolListView, UpdateLogView, PredictionListView

urlpatterns = [
    path('symbols/<int:pk>/', SymbolDetailView.as_view(), name='symbol-detail'),
    path('group/<int:pk>/', GroupSymbolDetailView.as_view(), name='group-detail'),
    path('group-symbols/', GroupSymbolListView.as_view(), name='group-symbols-list'),
    path('update-log/', UpdateLogView.as_view(), name='update-log'),
    path('prediction/', PredictionListView.as_view(), name='prediction '),
]