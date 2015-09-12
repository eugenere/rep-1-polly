import json

from django.http import HttpResponse

def indexJson(request):
    data = {}
    data['name'] = 'first json request'
    return HttpResponse(json.dumps(data), content_type="application/json")

def index(request):
    return HttpResponse('researchs index')

