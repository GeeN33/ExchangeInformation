import requests
from django.db.models import F
from datetime import datetime
from s_binance.models import Symbol, SymbolsInfo, SymbolError, Prediction


def fetch_binance_data():
    # fetch_binance_data_spot
    url = "https://api.binance.com/api/v3/exchangeInfo"
    response = requests.get(url)
    exchange_info = response.json()

    symbolException=['USDPUSDT','TUSDUSDT','BUSDUSDT','USDCUSDT']

    info = SymbolsInfo.objects.create()
    start = datetime.now()
    count_new = 0
    for symbol_data in exchange_info['symbols']:
        if(symbol_data['quoteAsset'] == 'USDT' and symbol_data['symbol'] not in symbolException):
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
