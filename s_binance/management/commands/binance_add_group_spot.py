from django.core.management.base import BaseCommand, CommandError

from s_binance.models import Symbol, Group


class Command(BaseCommand):
    help = 'binance_add_group_spot'

    def handle(self, *args, **options):
        symbols = Symbol.objects.all()

        partss = [symbols[i:i + 170] for i in range(0, len(symbols), 170)]

        for parts in partss:
            print(parts[0].symbol ,len(parts))
            group = Group.objects.get_or_create(name = parts[0].symbol)[0]
            for symbol in parts:
                group.symbols.add(symbol)
        # namesymbols = ['BTCUSDT',
        #                 'ETHUSDT',
        #                 'BCHUSDT',
        #                 'XRPUSDT',
        #                 'EOSUSDT',
        #                 'LTCUSDT',
        #                 'TRXUSDT',
        #                 'ETCUSDT',
        #                 'LINKUSDT',
        #                 'XLMUSDT',
        #                 'ADAUSDT',
        #                 'XMRUSDT',
        #                 'DASHUSDT',
        #                 'ZECUSDT',
        #                 'XTZUSDT',
        #                 'BNBUSDT',
        #                 'ATOMUSDT',
        #                 'ONTUSDT']
        # group = Group.objects.get_or_create(name='TEST')[0]
        #
        # for name in namesymbols:
        #     symbol = Symbol.objects.filter(symbol=name).last()
        #     group.symbols.add(symbol)
        #


