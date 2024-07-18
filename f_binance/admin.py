from django.contrib import admin
from .models import Symbol, Group, SymbolsInfo, SymbolError

admin.site.register(Symbol)

admin.site.register(Group)

admin.site.register(SymbolsInfo)

admin.site.register(SymbolError)