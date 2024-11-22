from django.contrib import admin
from .models import Currencies, CurrencyPairs


class ExchangeRateAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)
        
    search_fields = ['currency_pairs']


admin.site.register(Currencies)
admin.site.register(CurrencyPairs, ExchangeRateAdmin)