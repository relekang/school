
from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.http import HttpResponsePermanentRedirect

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'app.frontpage.views.frontpage'),
    (r'^profiles/me/$', 'app.frontpage.views.frontpage'),
    (r'^notes/', include('app.notes.urls')),
    (r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('',
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    url(r'^accounts/profile/$', lambda r: HttpResponsePermanentRedirect('/profiles/me')),
    url(r'^accounts/$', lambda r: HttpResponsePermanentRedirect('/profiles/me')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

