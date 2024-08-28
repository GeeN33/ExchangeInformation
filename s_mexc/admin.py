from django.contrib import admin
from .models import Symbol, SymbolsInfo, SymbolError, Log, Proxy, Prediction, Group, SubGroup


@admin.register(Symbol)
class SymbolAdmin(admin.ModelAdmin):
    model = Symbol
    list_display = ('symbol', 'status', )
    search_fields = ('symbol',)
    list_filter = [
        'status',
    ]

admin.site.register(Group)

admin.site.register(SubGroup)

admin.site.register(SymbolsInfo)

admin.site.register(SymbolError)

admin.site.register(Log)

admin.site.register(Proxy)

admin.site.register(Prediction)
