from django.urls import include, re_path, path
import CurrencyExchangeProject.views
from django.contrib import admin

# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', CurrencyExchangeProject.views.index, name='index'),
    path('exchange', CurrencyExchangeProject.views.get_exchange_rates, name='Exchange rate'),
    path('currencies', CurrencyExchangeProject.views.get_currencies, name='All currencies')
]