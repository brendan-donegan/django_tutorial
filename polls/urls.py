from django.conf.urls import patterns, url

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'django_tutorial.views.home', name='home'),
    # url(r'^django_tutorial/', include('django_tutorial.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
