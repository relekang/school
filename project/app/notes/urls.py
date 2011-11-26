from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.notes.views',
    (r'^$', 'list'),
    (r'^timestamp/$', 'timestamp'),
    (r'^(?P<id>\d+)/preview/$', 'preview'),
    (r'^(?P<id>\d+)/$', 'view'),
    (r'^(?P<course>.*)/$', 'list'),
)