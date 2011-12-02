from django.conf.urls.defaults import patterns

urlpatterns = patterns('app.algorithms.views',
    (r'^$', 'list'),
    (r'^edit/runningtime/$', 'edit_running_time'),
    (r'^(?P<tag>.*)/$', 'list'),
)