"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import django
from django.test import TestCase
from CurrencyExchangeProject.models import Currencies, CurrencyPairs
from django.test import Client
from rest_framework.views import status
from django.core.management import call_command
from CurrencyExchangeProject.views import get_exchange_rates

# TODO: Configure your database in settings.py and sync before running tests.

class CurrencyExchangeTests(TestCase):
    """Tests for the Currency Exchange application."""

    # Django requires an explicit setup() when running tests in PTVS
    @classmethod
    def setUpClass(cls):
        super(CurrencyExchangeTests, cls).setUpClass()
        django.setup()
        # create local database and populate it
        call_command('fetch_exchange_rates')

    def test_get_currencies(self):
        """Test GET all curencies in database."""
        c = Client()
        codes = [{'code': 'EUR'}, {'code': 'USD'}, {'code': 'PLN'}, {'code': 'JPY'}]
        response = c.get('/currencies')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for code in codes:
            self.assertIn(code, response.data)
            
    def test_get_exchange_rates(self):
        """Test GET exchange rates for a currency pair."""
        c = Client()
        test_currency_pair = 'EURJPY'
        symbol_end = '=X'
        expected_symbol = test_currency_pair + symbol_end
        response = c.get(f'/exchange?currency={test_currency_pair}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(expected_symbol, response.data['Symbol'])

