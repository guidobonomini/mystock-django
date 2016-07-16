from django.shortcuts import render
from stock.services import get_stock

def index(request):
    
    stockPrices = get_stock()
    return render(request, 'stockPrices.html', {'stock': stockPrices})
