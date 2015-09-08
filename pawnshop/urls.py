from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^index0$', views.index, name='index0'),
	url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^new_slave2/', views.NewSlaveView.as_view(), name='new_slave2'),
	url(r'^new_slave/', views.NewSlaveFormView.as_view(), name='new_slave'),
	url(r'^new_trash/', views.NewTrashView.as_view(), name='new_trash'),
	url(r'^submit_handler/', views.submit_handler, name='submit_handler'),
]