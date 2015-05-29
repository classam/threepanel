from django.conf.urls import patterns, include, url
from comics.feeds import LatestEntriesFeed

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'threepanel.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'comics.views.home', name='home'),
    url(r'^manage', 'comics.views.manage', name='manage'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^comics/', include('comics.urls')),
    url(r'^subscribe/', include('publish.urls')),
    url(r'^pages/', include('pages.urls')),
    url(r'^subscribe$', 'publish.views.subscribe'),
    url(r'rss.xml', LatestEntriesFeed())
)
