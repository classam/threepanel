from django.conf.urls import patterns, url

EMAIL = "(?P<email>[-_\w\.@]+)"
VERIFICATION_CODE = "(?P<verification_code>[-_\w]+)"

urlpatterns = patterns('',
    url(r'^subscribe_email$', 'publish.views.subscribe_email', name='subscribe_email'),
    url(r'^unsubscribe_email$', 'publish.views.unsubscribe_email', name='unsubscribe_email'),
    url(r'^verify/'+EMAIL+'/'+VERIFICATION_CODE+'$', 'publish.views.verify', name='verify'),
    url(r'^subscribe$', 'publish.views.subscribe', name='subscribe'),
    url(r'^bad_email$', 'publish.views.bad_email', name='bad_email'),
)
