from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^welcome', views.fakeRequest, name='welcome'),
    url(r'^home', views.fakeRequest, name='home'),

    url(r'^cashier/create', views.CreateCashier.as_view(), name='cashier-create'),
    url(r'^cashier/update', views.fakeRequest, name='cashier-update'),
    url(r'^cashier/description', views.fakeRequest, name='cashier-description'),
    url(r'^cashiers/list', views.fakeRequest, name='cashiers-list'),

    url(r'^client/create', views.CreateClient.as_view(), name='client-create'),
    url(r'^client/update', views.fakeRequest, name='client-update'),
    url(r'^client/description', views.fakeRequest, name='client-description'),
    url(r'^clients/list', views.fakeRequest, name='clients-list'),

    url(r'^pledge/create', views.CreatePledge.as_view(), name='pledge-create'),
    url(r'^pledge/update', views.fakeRequest, name='pledge-update'),
    url(r'^pledge/description', views.fakeRequest, name='pledge-description'),
    url(r'^pledges/list', views.fakeRequest, name='pledges-list'),

    url(r'^$', views.index, name='index'),
]
