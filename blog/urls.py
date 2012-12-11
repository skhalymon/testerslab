from django.conf.urls import patterns, url
from django.views.generic.simple import direct_to_template

from blog.views import LatestEntries


urlpatterns = patterns('blog.views',
    url(
        r'^$',
        'index',
        name='index'
    ),
    url(
        r'^about/$',
        direct_to_template,
        {
            'template': 'about.html',
            'extra_context': {
                'page_type': 'active',
            }
        },
        name='about'
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
