
from django.core.management.base import BaseCommand, CommandError

from s_mexc.models import Symbol, Group, Prediction, SubGroup


class Command(BaseCommand):
    help = 'mexc_add_group_spot'

    def handle(self, *args, **options):
        symbols = Symbol.objects.all()

        partss = [symbols[i:i + 190] for i in range(0, len(symbols), 190)]
        k = 0
        subgroup = None
        group = None
        for parts in partss:
            k += 1
            print('group', parts[0].symbol , len(parts))
            group = Group.objects.get_or_create(name = parts[0].symbol)[0]
            print(k, '=========== group')
            i = 1
            for symbol in parts:
                if i == 1:
                    subgroup = SubGroup.objects.get_or_create(group=group, name=symbol.symbol)[0]
                    print('/////////// subgroup')
                i += 1
                if i > 10: i = 1

                if subgroup:
                    subgroup.symbols.add(symbol)
                    print(i, symbol.symbol)

        print('all', len(partss))