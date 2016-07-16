from django.shortcuts import render
from homepage.searchYTS import *
from homepage.searchKickass import *

def index(request):
    return render(request, 'home.html')

def searchYTS(request, query, currentPage):
    
    search = SearchYTS()
    result = search.searchYTS(query, currentPage)
    return render(request, 'search.html', {'movies': result[1], 'pages': [0 for x in range(result[0])]})


def searchKickass(request, query, currentPage):
    
    search = SearchKickass()
    result = search.searchKickass(query, currentPage)
    return render(request, 'search.html', {'movies': result[1], 'pages': [0 for x in range(result[0])]})
