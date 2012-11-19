from django.conf.urls import patterns, url


urlpatterns = patterns('blog.views',
        url(r'^$', 'index'),
        url(r'^tag/(?P<tag>\w+)$', 'tag'),
        url(r'^category/(?P<cat>\w+)$', 'category'),
        url(r'^(?P<slug>[^\.]+)', 'post'),
)
