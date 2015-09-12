from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^indexJson', views.indexJson, name='indexJson'),
    url(r'^', views.index, name='index'),
]
