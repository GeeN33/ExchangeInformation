import datetime
from django.utils import timezone
import json
import requests
from dateutil import parser

from f_binance.models import Prediction as PredictionF
from s_binance.models import Prediction as PredictionS

API_URL="http://147.45.228.133:8444/predict/"


def max_min_bars(bars):
    max = 0
    min = bars[0]['high']
    for bar in bars:
        if bar['high'] > max:
            max = bar['high']
        if bar['low'] < min:
            min = bar['low']
    return max, min

def max_min_delta(bars):
    max = 0
    min = bars[0]
    for bar in bars:
        if bar > max:
            max = bar
        if bar < min:
            min = bar
    return max, min

def add_delta(bars):
    deltas = []
    delta = 1000
    for bar in bars:
        deltas.append(delta)
        delta = delta + bar['delta_buy'] - bar['delta_sell']
        deltas.append(delta)
    return deltas

def convert_bars_to_one(high, low, height, max, min):
    high_y = 0

    low_y = 0

    if max - min == 0: return high_y, low_y

    high_y = (high - min) * (height / (max - min))

    low_y = (low - min) * (height / (max - min))

    return high_y, low_y

def convert_deltas_to_one(high, height, max, min):

    high_y = 0

    if max - min == 0: return high_y

    high_y = (high - min) * (height / (max - min))

    return high_y


def sort_symbols_coin(isspot, per):
    # datas = read_json()
    symbols_data = []
    API_URL = "https://api.chillacoin.ru/for/predict/"
    response = requests.get(API_URL, params={'isspot': isspot, 'per': per})

    if response.status_code == 200:
        datas = response.json()
        symbols = []
        for data in datas:
            if data['symbol'] not in symbols:
               symbols.append(data['symbol'])

        for symbol in symbols:
            coin = {}
            bars = []
            for data in datas:
                if symbol == data['symbol']:
                    bars.append(data)
            bars_sorted = sorted(bars, key=lambda x: parser.isoparse(x['datetime']))
            coin['symbol'] = symbol
            coin['bars'] =  bars_sorted[-20:]

            symbols_data.append(coin)

    return symbols_data

def sort_bars(bars):

    max, min = max_min_bars(bars)

    deltas = add_delta(bars)

    max_d, min_d = max_min_delta(deltas)

    barss = []
    height = 1
    for bar in bars:
        high_y, low_y = convert_bars_to_one(bar['high'], bar['low'], height, max, min)
        barss.append(high_y)
        barss.append(low_y)

    for bar in deltas:
        high_y= convert_deltas_to_one(bar, height, max_d, min_d)
        barss.append(high_y)

    return  barss

def get_coin_delta(isspot, per):
    symbols_data = sort_symbols_coin(True, per)
    symbols = []
    bars = []
    for data in symbols_data:
        symbols.append(data['symbol'])
        barss =  sort_bars(data['bars'])
        bars.append(barss)

    return bars, symbols

def prediction(isspot, per):

    bars, symbols = get_coin_delta(isspot, per)

    headers = {
        'Content-Type': 'application/json'
    }

    payload = json.dumps({
        "bars": bars,
        "symbols": symbols
    }, indent=False)

    response = requests.request("POST", API_URL, headers=headers, data=payload, verify=False)

    if response.status_code == 200:
        return response.json()['predictions']
    else:
        return []

def go_prediction(per):
    date = datetime.datetime.now()
    current_date = timezone.now()
    predictions = prediction(False, per)
    for predict in predictions:
        coin = PredictionF.objects.filter(symbol__symbol=predict['symbol']).last()
        if coin:
            coin.predicted_class = predict['predicted_class']
            coin.probability = predict['probability']
            coin.probabilities = predict['probabilities']
            coin.up_date = current_date
            coin.save()

    predictions = prediction(True, per)
    for predict in predictions:
        coin = PredictionS.objects.filter(symbol__symbol=predict['symbol']).last()
        if coin:
            coin.predicted_class = predict['predicted_class']
            coin.probability = predict['probability']
            coin.probabilities = predict['probabilities']
            coin.up_date = current_date
            coin.save()

    return f'predictions finish {datetime.datetime.now() - date}'