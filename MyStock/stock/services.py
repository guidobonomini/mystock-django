import requests
import json

def get_stock():
    
    url = 'http://marketdata.websol.barchart.com/getQuote.json?key=46447333b150fc404ba865c412fe70e0&symbols=IBM,GOOGL,AAPL,PFE,AMZN,MSFT,INTC,EBAY,FB,YHOO,CSCO'

    result = requests.get(url)
    stockPrices = json.loads(result.text)
    return stockPrices


def get_historicalPrice(symbol):

    url = 'http://marketdata.websol.barchart.com/getHistory.json?key=46447333b150fc404ba865c412fe70e0&symbol=' + symbol +'&type=weekly&startDate=20150714000000'
    result = requests.get(url)
    historicalPrice = json.loads(result.text)
    return historicalPrice
