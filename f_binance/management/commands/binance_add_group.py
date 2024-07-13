from django.core.management.base import BaseCommand, CommandError

from f_binance.models import Symbol, Group


class Command(BaseCommand):
    help = 'binance_add_group'

    def handle(self, *args, **options):
        symbols = Symbol.objects.all()

        partss = [symbols[i:i + 160] for i in range(0, len(symbols), 160)]

        for parts in partss:
            group = Group.objects.get_or_create(name = parts[0].symbol)[0]
            for symbol in parts:
                group.symbol.add(symbol)


