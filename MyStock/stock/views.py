from django.shortcuts import render
from stock.services import *
from stock.charts import *

def index(request):
    
    stockPrices = get_stock()
    return render(request, 'stockPrices.html', {'stock': stockPrices})

def stockDetail(request, symbol):
    
    historicalPrice = get_historicalPrice(symbol)
    loadHistoricalChart(historicalPrice)
    
    return render(request, 'stockDetail.html')
