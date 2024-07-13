import requests
from django.db.models import F
from datetime import datetime
from f_binance.models import Symbol, Filter, SymbolsInfo, SymbolError


def fetch_binance_data():
    url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
    response = requests.get(url)
    exchange_info = response.json()

    info = SymbolsInfo.objects.create()
    start = datetime.now()
    count_new = 0
    for symbol_data in exchange_info['symbols']:

        try:

            filters = symbol_data.pop('filters', [])

            symbol, created = Symbol.objects.update_or_create(
                symbol = symbol_data['symbol'],
                defaults = symbol_data
            )
            if created:
                count_new += 1

            filterTypes_bd_list = list(Filter.objects.filter(symbol = symbol).values_list('filterType', flat=True))

            filterTypes_list = [filter['filterType'] for filter in filters]

            # Delete filters
            for filter in filterTypes_bd_list:
                if filter not in filterTypes_list:
                    Filter.objects.filter(symbol = symbol, filterType = filter).delete()

            # Update or create filters
            for filter in filters:
                Filter.objects.update_or_create(
                    symbol = symbol, filterType = filter['filterType'], defaults = filter)

        except Exception as e:
            SymbolError.objects.create(
                symbols_info = info,
                symbol = symbol_data['symbol'],
                error = str(e)
            )
            print(e)
    info.count_new = count_new
    info.time_spent = str(datetime.now() - start)
    info.save()

    return f'count new: {count_new}, time spent: {str(datetime.now() - start)}, updated: {str(datetime.now())}'
