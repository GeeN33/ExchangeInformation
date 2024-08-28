from datetime import datetime

import requests

from .models import Symbol, SymbolsInfo, Prediction, SymbolError


def fetch_market_symbols():
    url = "https://api.mexc.com/api/v3/exchangeInfo"
    response = requests.get(url)
    exchange_info = response.json()
    info = SymbolsInfo.objects.create()
    start = datetime.now()
    count_new = 0
    for symbol_data in exchange_info['symbols']:

        if symbol_data['symbol'].endswith('USDT') and symbol_data['isSpotTradingAllowed']:
            try:
                symbol, created = Symbol.objects.update_or_create(
                    symbol=symbol_data['symbol'],
                    defaults=symbol_data
                )
                if created:
                    print(count_new, symbol_data['symbol'])
                    Prediction.objects.create(symbol=symbol)
                    count_new += 1

            except Exception as e:
                SymbolError.objects.create(
                    symbols_info=info,
                    symbol=symbol_data['symbol'],
                    error=str(e)
                )
                print(e)

    info.count_new = count_new
    info.time_spent = str(datetime.now() - start)
    info.save()

    return f'count new: {count_new}, time spent: {str(datetime.now() - start)}, updated: {str(datetime.now())}'