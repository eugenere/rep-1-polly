from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import *
from django.core.urlresolvers import reverse, reverse_lazy

import logging
from . import models


log = logging.getLogger('dbg')


def index(request):
    log.debug('limbo index')
    return HttpResponse('welcome to limbo(popshow)')


def index1(request):
    context = {
        'varName': 'var value',
    }
    return render(request, 'index1.html', context)


def fakeRequest(request):
    log.debug('not ready yet')
    return HttpResponse('not ready yet')


class CreateCashier(CreateView):
    model = models.Cashier
    fields = [
            'login',
            'key',
            'first_name',
            'family',
            'surname',
            'passportCode',
            'address',
    ]
    def get_success_url(self):
        return reverse("popshop:cashiers-list") 


class CreateClient(CreateView):
    model = models.Client
    fields = [
            'first_name',
            'family',
            'surname',
            'passportCode',
            'address',
    ]
    def get_success_url(self):
        return reverse("popshop:clients-list") 


class CreatePledge(CreateView):
    model = models.Pledge
    fields = [
            'pledger',
            'description',
            'price',
            'term',
    ]
	
class CashiersList(ListView):
    model = models.Cashier
	
	