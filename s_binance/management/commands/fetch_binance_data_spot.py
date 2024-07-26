from django.core.management.base import BaseCommand, CommandError

from s_binance.service import fetch_binance_data


class Command(BaseCommand):
    help = 'fetch_binance_data_spot'

    def handle(self, *args, **options):
        res = fetch_binance_data()
        print(res)


