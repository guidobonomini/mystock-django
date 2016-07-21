from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'stockPrices/$', views.index, name='index'),
    url(r'stockDetail/(?P<symbol>\w+)/$', views.stockDetail, name='stockDetail'),
]
