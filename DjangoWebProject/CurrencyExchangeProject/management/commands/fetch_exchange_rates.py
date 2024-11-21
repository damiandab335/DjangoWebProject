from typing import List
from django.core.management.base import BaseCommand
from CurrencyExchangeProject.models import Currencies, CurrencyPairs
import yfinance as yf
from pandas.core.frame import DataFrame

CURRENCIES = [
    'EUR',
    'USD',
    'PLN',
    'JPY'
    ]

def create_currency_pair_symbols(currencies: List[str]) -> List[str]:
    symbol_end = '=X'
    currency_pair_symbols = []
    while(currencies):
        first_symbol = currencies.pop(0)
        for second_symbol in currencies:
            combination1 = first_symbol+second_symbol+symbol_end
            combination2 = second_symbol+first_symbol+symbol_end
            combination1 = combination1.removeprefix("USD")
            combination2 = combination2.removeprefix("USD")
            currency_pair_symbols.append(combination1)
            currency_pair_symbols.append(combination2)
    return currency_pair_symbols


class Command(BaseCommand):
    help = 'Fetch data from the external API and populate the database'
    
    def add_arguments(self, parser):
        parser.add_argument('-c', '--currencies', nargs="*", default=CURRENCIES, help='List of currencies to create exchange rates database for')
        parser.add_argument('-s', '--start_date', default="2024-10-19", type=str, help='Start date to load exchange rates')
        parser.add_argument('-e', '--end_date', default="2024-11-19", type=str, help='End date to load exchange rates')

    def handle(self, *args, **kwargs):
        for currency in kwargs['currencies']:
            Currencies.objects.update_or_create(
                    code=currency
                )
        currency_pairs = create_currency_pair_symbols(kwargs['currencies'])
        for currency_pair_symbol in currency_pairs:
            self.download_currency_pair_data(currency_pair_symbol, kwargs['start_date'], kwargs['end_date'])
            
    def download_currency_pair_data(self, currency_pair_symbol: str, start_date: str, end_date: str):
        exchange_data = yf.download(currency_pair_symbol, start=start_date, end=end_date)
        if type(exchange_data) is DataFrame and not exchange_data.empty:
            exchange_data_dict = exchange_data['Close'].to_dict()[currency_pair_symbol]
            for timestamp, exchange_rate in exchange_data_dict.items():
                CurrencyPairs.objects.update_or_create(
                    exchange_date=timestamp.date(),
                    currency_pairs = currency_pair_symbol,
                    exchange_rates = exchange_rate
                )
                
            self.stdout.write(self.style.SUCCESS(f'Successfully populated the database for currency pair symbol: {currency_pair_symbol}'))
        else:
            self.stdout.write(self.style.ERROR(f'Wrong data type or data is empty, failed to populate database '
                                               f'for currency pair symbol: {currency_pair_symbol}'))