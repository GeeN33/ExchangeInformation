from django.db import models

class Symbol(models.Model):
    symbol = models.CharField(max_length=100, unique=True)
    pair = models.CharField(max_length=100)
    contractType = models.CharField(max_length=100)
    deliveryDate = models.BigIntegerField()
    onboardDate = models.BigIntegerField()
    status = models.CharField(max_length=100)
    maintMarginPercent = models.CharField(max_length=100)
    requiredMarginPercent = models.CharField(max_length=100)
    baseAsset = models.CharField(max_length=100)
    quoteAsset = models.CharField(max_length=100)
    marginAsset = models.CharField(max_length=100)
    pricePrecision = models.IntegerField()
    quantityPrecision = models.IntegerField()
    baseAssetPrecision = models.IntegerField()
    quotePrecision = models.IntegerField()
    underlyingType = models.CharField(max_length=100, null=True, blank=True)
    underlyingSubType = models.JSONField(null=True, blank=True)
    settlePlan = models.IntegerField(null=True, blank=True)
    triggerProtect = models.CharField(max_length=100, null=True, blank=True)
    liquidationFee = models.CharField(max_length=100, null=True, blank=True)
    marketTakeBound = models.CharField(max_length=100, null=True, blank=True)
    maxMoveOrderLimit = models.IntegerField(null=True, blank=True)
    orderTypes = models.JSONField(null=True, blank=True)
    timeInForce = models.JSONField(null=True, blank=True)
    filters = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f'{self.symbol}'

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
    symbols = models.ManyToManyField(Symbol)
    name = models.CharField(max_length=100, null=True, blank=True )
    proxy_active = models.BooleanField(default=False)
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