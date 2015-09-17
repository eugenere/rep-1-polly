from __future__ import print_function
from cms.sitemaps import CMSSitemap
from django.conf.urls import *  # NOQA
from django.conf.urls.i18n import i18n_patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf import settings

from cmn.etc import dbg

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^djangojs/', include('djangojs.urls')),
    url(r'^researchs/', include('researchs.urls', namespace="researchs")),
    url(r'^pawnshop/', include('pawnshop.urls', namespace="pawnshop")),
    url(r'^popshop/', include('popshop.urls', namespace="popshop")),
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

import logging
log = logging.getLogger('dbg')

log.debug('resolve url')
dbg('resolve url')
