import json

from django.core.management.base import BaseCommand, CommandError
import requests
from datetime import datetime
class Command(BaseCommand):
    help = 'add_api_coin_delta'

    def handle(self, *args, **options):
        # url = "https://chillacoin.ru/f-binance/group-symbols/?format=json"
        API_URL = "https://api.chillacoin.ru/symbols/"

        # response = requests.get(url)
        # groups = response.json()
        symbols = ['BTCUSDT',
                       'ETHUSDT',
                       'BCHUSDT',
                       'XRPUSDT',
                       'EOSUSDT',
                       'LTCUSDT',
                       'TRXUSDT',
                       'ETCUSDT',
                       'LINKUSDT',
                       'XLMUSDT',
                       'ADAUSDT',
                       'XMRUSDT',
                       'DASHUSDT',
                       'ZECUSDT',
                       'XTZUSDT',
                       'BNBUSDT',
                       'ATOMUSDT',
                       'ONTUSDT']

        periods = [5, 60]
        count = 0
        for symbol in symbols:
            count += 1
            print(symbol, count)
            for per in periods:
                for i in range(1, 72):
                    data = {
                          "symbol": symbol,
                          "exchange": "binance",
                          "isspot": False,
                          "per": per,
                          "datetime": datetime.now().isoformat(),
                          "open": 0,
                          "high": 0,
                          "low": 0,
                          "close": 0,
                          "delta_buy": 0,
                          "delta_sell": 0,
                          "index": i
                    }
                    try:
                         response = requests.post(API_URL, headers={'Content-Type': 'application/json'}, data=json.dumps(data))
                         response.raise_for_status()
                    except Exception as e:
                         print('Ошибка при загрузке страницы: ' + str(e))
