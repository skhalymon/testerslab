import operator

from django.shortcuts import render, get_object_or_404
from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.db.models import Q
from blog.models import Post, Category


def index(request):
    latest_posts = Post.objects.filter(published=True).order_by('-created')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'blog.html', context)


def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'post.html', context)


def tag(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'posts': posts,
        'tag': tag,
    }
    return render(request, 'tag.html', context)


def category(request, slug):
    posts = Post.objects.filter(categories__slug=slug)
    try:
        c = Category.objects.get(slug=slug)
        name = c.name
    except Category.DoesNotExist:
        name = 'default'
    context = {
        'posts': posts,
        'slug': slug,
        'cat': name,
    }
    return render(request, 'category.html', context)


def archive(request):
    all_posts = Post.objects.filter(published=True).order_by('-created')
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'archive.html', context)


def search(request):
    errors = []
    if 'q' in request.GET:
        query = request.GET['q']
        query = handle_keywords(query)
        if not query:
            errors.append('Enter minimum 3 characters')
        else:
            query_results = Post.objects.filter(
                reduce(operator.and_, (
                    Q(title__icontains=q) for q in query)) |
                reduce(operator.and_, (
                    Q(content__icontains=q) for q in query)),
                published=True,
            ).order_by('created').distinct()
            context = {
                'query_results': query_results,
            }
            return render(request, 'results.html', context)
    return render(request, 'blog.html', {'errors': errors})


def handle_keywords(keywords):
    if (
        keywords.startswith('"') and keywords.endswith('"')) or (
            keywords.startswith("'") and keywords.endswith("'")):
        return [keywords[1:-1]]
    return set(t for t in keywords.split(" ") if len(t) >= 3)


class LatestEntries(Feed):
    title = "xxx"
    link = "/blog/feed/"
    description = " xxxxxxxx "

    def items(self):
        return Post.objects.filter(published=True).order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('post', args=[item.slug])
