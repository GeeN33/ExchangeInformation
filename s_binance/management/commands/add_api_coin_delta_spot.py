import json

from django.core.management.base import BaseCommand, CommandError
import requests
from datetime import datetime

from s_binance.models import Group, Symbol


class Command(BaseCommand):
    help = 'add_api_coin_delta_spot'

    def handle(self, *args, **options):
        groups = Group.objects.all()

        for group in groups:
            for symbol in group.symbols.all():
                if(symbol.symbol == 'BUSDUSDT'):
                    print(group.pk,  symbol.symbol)

        # symbols = Symbol.objects.all()
        # for symbol in symbols:
        #     if (symbol.symbol == 'USDPUSDT'):
        #         print(symbol.symbol)
