import requests

from f_binance.models import Symbol, Filter


def fetch_binance_data():
    url = "https://fapi.binance.com/fapi/v1/exchangeInfo"
    response = requests.get(url)
    exchange_info = response.json()

    for symbol_data in exchange_info['symbols']:
        symbol, created = Symbol.objects.update_or_create(
            symbol=symbol_data['symbol'],
            defaults={
                'pair': symbol_data['pair'],
                'contract_type': symbol_data['contractType'],
                'delivery_date': symbol_data['deliveryDate'],
                'onboard_date': symbol_data['onboardDate'],
                'status': symbol_data['status'],
                'maint_margin_percent': symbol_data['maintMarginPercent'],
                'required_margin_percent': symbol_data['requiredMarginPercent'],
                'base_asset': symbol_data['baseAsset'],
                'quote_asset': symbol_data['quoteAsset'],
                'margin_asset': symbol_data['marginAsset'],
                'price_precision': symbol_data['pricePrecision'],
                'quantity_precision': symbol_data['quantityPrecision'],
                'base_asset_precision': symbol_data['baseAssetPrecision'],
                'quote_precision': symbol_data['quotePrecision'],
                'underlying_type': symbol_data.get('underlyingType'),
                'underlying_sub_type': symbol_data.get('underlyingSubType'),
                'settle_plan': symbol_data.get('settlePlan'),
                'trigger_protect': symbol_data.get('triggerProtect'),
                'liquidation_fee': symbol_data.get('liquidationFee'),
                'market_take_bound': symbol_data.get('marketTakeBound'),
                'max_move_order_limit': symbol_data.get('maxMoveOrderLimit'),
                'order_types': symbol_data['orderTypes'],
                'time_in_force': symbol_data['timeInForce'],
            }
        )

        # Удаляем старые фильтры и добавляем новые
        symbol.filters.clear()
        for filter_data in symbol_data['filters']:
            filter_obj, created = Filter.objects.update_or_create(
                filter_type=filter_data['filterType'],
                defaults={k: filter_data.get(k) for k in filter_data if k != 'filterType'}
            )
            symbol.filters.add(filter_obj)