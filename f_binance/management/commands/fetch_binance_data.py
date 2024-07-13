from django.core.management.base import BaseCommand, CommandError

from f_binance.service import fetch_binance_data


class Command(BaseCommand):
    help = 'fetch_binance_data'

    def handle(self, *args, **options):
        fetch_binance_data()


