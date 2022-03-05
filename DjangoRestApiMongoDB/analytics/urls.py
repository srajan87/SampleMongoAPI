from django.conf.urls import url 
from analytics import views 
 
urlpatterns = [ 
    url(r'^analytics/accounts$', views.accounts_list),
    url(r'^analytics/accounts/(?P<pk>[0-9]+)$', views.accounts_detail),
    url(r'^analytics/accounts/registered$', views.accounts_list_registered)
]