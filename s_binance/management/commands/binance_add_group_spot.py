from django.core.management.base import BaseCommand, CommandError

from s_binance.models import Symbol, Group, Prediction


class Command(BaseCommand):
    help = 'binance_add_group_spot'

    def handle(self, *args, **options):
        symbols = Symbol.objects.all()
        # for symbol in symbols:
        #     Prediction.objects.create(symbol=symbol)
        #     print(symbol.symbol)

        # partss = [symbols[i:i + 170] for i in range(0, len(symbols), 170)]
        #
        # for parts in partss:
        #     print(parts[0].symbol ,len(parts))
        #     group = Group.objects.get_or_create(name = parts[0].symbol)[0]
        #     for symbol in parts:
        #         group.symbols.add(symbol)



