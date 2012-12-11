from django.conf.urls import patterns, url
from blog.views import LatestEntries


urlpatterns = patterns('blog.views',
    url(
        r'^$',
        'index',
        name='index'
    ),
    url(
        r'^search/$',
        'search',
        name='search'
    ),
    url(
        r'^archive/$',
        'archive',
        name='archive'
    ),
    url(
        r'^feed/$',
        LatestEntries(),
        name='rss'
    ),
    url(
        r'^tag/(?P<tag>\w+)/$',
        'tag',
        name='tag'
    ),
    url(
        r'^category/(?P<slug>[^\.]+)/$',
        'category',
        name='category'
    ),
    url(
        r'^(?P<slug>[^\.]+)/$',
        'post',
        name='post'
    ),
)
