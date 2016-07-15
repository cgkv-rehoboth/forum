# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

import spirit.urls

urlpatterns = [
    url(r'^forum/', include(spirit.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
