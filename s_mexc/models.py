from django.db import models

class Symbol(models.Model):
    symbol = models.CharField(max_length=50)
    status = models.CharField(max_length=10)
    baseAsset = models.CharField(max_length=50)
    baseAssetPrecision = models.IntegerField()
    quoteAsset = models.CharField(max_length=50)
    quotePrecision = models.IntegerField()
    quoteAssetPrecision = models.IntegerField()
    baseCommissionPrecision = models.IntegerField()
    quoteCommissionPrecision = models.IntegerField()
    orderTypes = models.JSONField()
    isSpotTradingAllowed = models.BooleanField()
    isMarginTradingAllowed = models.BooleanField()
    quoteAmountPrecision = models.CharField(max_length=50)
    baseSizePrecision = models.CharField(max_length=50)
    permissions = models.JSONField()
    filters = models.JSONField(default=list, blank=True)  # Assuming filters is a list
    maxQuoteAmount = models.CharField(max_length=100)
    makerCommission = models.CharField(max_length=50)
    takerCommission = models.CharField(max_length=50)
    quoteAmountPrecisionMarket = models.CharField(max_length=100)
    maxQuoteAmountMarket = models.CharField(max_length=100)
    fullName = models.CharField(max_length=100)
    tradeSideType = models.IntegerField()

    def __str__(self):
        return self.symbol

class Proxy(models.Model):
    name = models.CharField(max_length=100, default='proxy')
    ip = models.CharField(max_length=100)
    port = models.IntegerField()
    login = models.CharField(max_length=100, null=True, blank=True )
    password = models.CharField(max_length=100, null=True, blank=True )

    def __str__(self):
        return f'{self.name}-{self.ip}:{self.port}'

class Group(models.Model):
    proxy = models.ForeignKey(Proxy, on_delete=models.SET_NULL, related_name='group', null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True )
    proxy_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}-{self.name}'

class SubGroup(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='subgroup', null=True, blank=True)
    symbols = models.ManyToManyField(Symbol)
    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.pk}-{self.name}'

class SymbolsInfo(models.Model):
    count_new = models.IntegerField(default=0)
    time_spent = models.CharField(max_length=100, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'time spent:{self.time_spent}, count new:{str(self.count_new)}, updated:{str(self.updated_at)}'

class SymbolError(models.Model):
    symbols_info = models.ForeignKey(SymbolsInfo, on_delete=models.CASCADE, related_name='symbol_error')
    symbol = models.CharField(max_length=100, null=True, blank=True)
    error = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'created:{self.created_at}'

class Log(models.Model):
    type = models.CharField(max_length=100, default='nunknown')
    description = models.TextField(default='unknown')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'created:{self.created_at}, type:{self.type}'

class Prediction(models.Model):
    symbol = models.ForeignKey(Symbol, on_delete=models.CASCADE, related_name='prediction')
    predicted_class = models.CharField(max_length=10, null=True, blank=True)
    probability = models.FloatField(null=True, blank=True)
    probabilities = models.JSONField(null=True, blank=True)
    up_date = models.DateTimeField(null=True, blank=True)