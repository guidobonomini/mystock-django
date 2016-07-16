from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'home/$', views.index, name='index'),
    url(r'searchYTS/(?P<query>\w+)/(?P<currentPage>[0-9]+)/$', views.searchYTS, name="searchYTS"),
    url(r'searchKickass/(?P<query>\w+)/(?P<currentPage>[0-9]+)/$', views.searchKickass, name="searchKickass"),
]
