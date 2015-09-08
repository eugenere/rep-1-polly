from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^pawnshop/', include('pawnshop.urls', namespace="pawnshop")),
    url(r'^', include('cms.urls')),
)

import logging
log = logging.getLogger('dbg')

log.debug('resolve url')
