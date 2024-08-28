from django.core.management.base import BaseCommand, CommandError

from s_mexc.service import fetch_market_symbols

class Command(BaseCommand):
    help = 'fetch_mexc_data_spot'

    def handle(self, *args, **options):
        res = fetch_market_symbols()
        print(res)


