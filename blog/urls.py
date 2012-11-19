from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
    url(
        r'^$',
        'index',
        name='index'
    ),
    url(
        r'^archive/$',
        'archive',
        name='archive'
    ),
    url(
        r'^tag/(?P<tag>\w+)/$',
        'tag',
        name='tag'
    ),
    url(
        r'^category/(?P<cat>\w+)/$',
        'category',
        name='category'
    ),
    url(
        r'^(?P<slug>[^\.]+)/$',
        'post',
        name='post'
    ),
)
