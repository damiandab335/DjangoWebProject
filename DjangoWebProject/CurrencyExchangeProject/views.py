from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import yfinance as yf
from typing import List
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from CurrencyExchangeProject.models import Currencies, CurrencyPairs
from django.core.exceptions import ObjectDoesNotExist


@api_view(['GET'])
def get_exchange_rates(request):
    symbol_end = '=X'
    currency_pair = request.GET.get('currency')
    if currency_pair is None:
        return Response("No arguments given", status.HTTP_204_NO_CONTENT)
    currency_pair = currency_pair.removeprefix("USD") + symbol_end
    try:
        exchange_rates = CurrencyPairs.objects.all().filter(currency_pairs=currency_pair).latest('exchange_date')
    except ObjectDoesNotExist:
        return Response("Empty", status.HTTP_204_NO_CONTENT)
    data = {
        'Date': exchange_rates.exchange_date,
        'Symbol': exchange_rates.currency_pairs,
        'Echange rate': exchange_rates.exchange_rates
    }
    return Response(data)


@api_view(['GET'])
def get_currencies(request):
    all_currencies = Currencies.objects.all()
    data = [{'code': currency_code.code} for currency_code in all_currencies]
    return Response(data)


def index(request):
    return render(
        request,
        "CurrencyExchangeProject/index.html",
        {
            'title' : "Currency Exchange Project",
            'message' : "Currency Exchange Project",
        }
    )
