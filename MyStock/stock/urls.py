from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'stockPrices/$', views.index, name='index'),
]
