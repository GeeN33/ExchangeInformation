from django.urls import path
from .views import SymbolDetailView, SymbolListView, GroupSymbolDetailView, GroupSymbolListView

urlpatterns = [
    path('symbols/', SymbolListView.as_view(), name='symbol-list-create'),
    path('symbols/<int:pk>/', SymbolDetailView.as_view(), name='symbol-detail'),
    path('group/<int:pk>/', GroupSymbolDetailView.as_view(), name='group-detail'),
    path('group-symbols/', GroupSymbolListView.as_view(), name='group-symbols-list'),
]