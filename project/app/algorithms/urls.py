from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.algorithms.views',
    (r'^$', 'list'),
    (r'^(?P<tag>.*)/$', 'list'),
)