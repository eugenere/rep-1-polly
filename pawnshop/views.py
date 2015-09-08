from django.http import HttpResponse
from django.views.generic import CreateView, FormView
from django.forms import ModelForm
from django.core.urlresolvers import reverse

from .models import Soul, Swag
from .forms import NewSoulForm

import logging
log = logging.getLogger('dbg')

def submit_handler(request):
	res = 'submit_handler'
	res += '<br>' + 'request.method: {0}'.format(request.method)
	
	form = NewSoulForm(request.POST)
	
	res += '<br>' + 'form.is_valid: {0}'.format(form.is_valid())
	
	if form.is_valid():
		form.save()
		res += '<br>' + 'res: ok'
	else:
		res += '<br>' + 'res: no'
	
	return HttpResponse(res)
	#return HttpResponseRedirect('/')

def index(request):
    log.debug('limbo')
    return HttpResponse('welcome to limbo')

def index2(request):
    log.debug('limbo')
    context = {
        'var': 1,
    }
    return render(request, 'index.html', context)

class NewSlaveFormView(FormView):
    form_class = NewSoulForm
    fields = ['name', 'key', 'kind']
    template_name = 'new_slave.html'
	
    def get_success_url(self):
        return reverse('pawnshop:index')
    def get_initial(self):
        return { 'kind': 'PM' }

class NewSlaveView(CreateView):
    model = Soul
    fields = ['name', 'key', 'kind']
    template_name = 'new_slave.html'
    def get_success_url(self):
        return reverse('pawnshop:index')
    def get_initial(self):
        return { 'kind': 'PM' }
	
class NewTrashView(CreateView):

    model = Swag
    fields = ['name', 'cost', 'owner']
    template_name = 'new_trash.html'

    def get_success_url(self):
        return reverse('pawnshop:index')
	