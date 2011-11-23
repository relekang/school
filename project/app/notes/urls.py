from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.notes.views',
    (r'^$', 'list'),
    (r'^(?P<id>\d+)/$', 'view'),
    (r'^(?P<course>.*)/$', 'list'),
)