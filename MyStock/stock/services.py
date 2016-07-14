import requests
import json

def get_stock():
    
    url = 'http://marketdata.websol.barchart.com/getQuote.json?key=46447333b150fc404ba865c412fe70e0&symbols=IBM,GOOGL,APPL,PFE,AMZN,MSFT,INTC,EBAY,FB,YHOO,CSCO'

    result = requests.get(url)
    stockPrices = json.loads(result.text)
    return stockPrices
