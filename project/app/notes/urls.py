from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.notes.views',
    (r'^$', 'list'),
    (r'^timestamp/$', 'timestamp'),
    (r'^tags/$', 'tags'),
    (r'^save/(?P<id>\d+)/$', 'save'),
    (r'^(?P<id>\d+)/preview/$', 'preview'),
    (r'^(?P<id>\d+)/edit/$', 'edit'),
    (r'^(?P<id>\d+)/$', 'view'),
    (r'^(?P<course>.*)/add/$', 'add'),
    (r'^(?P<course>.*)/$', 'list'),
)