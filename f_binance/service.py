import requests
from django.db.models import F
from datetime import datetime
from f_binance.models import Symbol, SymbolsInfo, SymbolError, Prediction


def fetch_binance_data():
    url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
    response = requests.get(url)
    exchange_info = response.json()

    info = SymbolsInfo.objects.create()
    start = datetime.now()
    count_new = 0
    for symbol_data in exchange_info['symbols']:

        try:
            symbol, created = Symbol.objects.update_or_create(
                symbol = symbol_data['symbol'],
                defaults = symbol_data
            )
            if created:
                Prediction.objects.create(symbol=symbol)
                count_new += 1

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
