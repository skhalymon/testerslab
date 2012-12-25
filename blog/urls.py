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
        r'^posts/(?P<user>\w+)/$',
        'posts_by_user',
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
        r'^about/$',
        'users',
        name='about'
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
