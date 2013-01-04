import json
import operator

from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.syndication.views import Feed
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.db.models import Q

from blog.models import Post, Category


def index(request):
    latest_posts = Post.objects.filter(published=True).order_by('-created')[:5]
    context = {
        'latest_posts': latest_posts,
        'page_type': 'highlight_index',
    }
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
    cat = get_object_or_404(Category, slug=slug)
    context = {
        'posts': posts,
        'slug': slug,
        'cat': cat.name,
    }
    return render(request, 'category.html', context)


def archive(request):
    all_posts = Post.objects.filter(published=True).order_by('-created')
    context = {
        'all_posts': all_posts,
        'page_type': 'highlight_archive',
    }
    return render(request, 'archive.html', context)


def users(request):
    users = User.objects.all().order_by('?')
    context = {'users': users}
    return render(request, 'about.html', context)


def posts_by_user(request, user):
    posts_by_user = Post.objects.filter(
        author__username=user,
        published=True,
    ).values('title', 'slug')
    return HttpResponse(
        json.dumps(list(posts_by_user)),
        mimetype='application/json'
    )


def search(request):
    errors = []
    if 'q' in request.GET:
        query = search_term = request.GET['q']
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
                'search_term': search_term,
                'query_results': query_results,
            }
            return render(request, 'results.html', context)
    return render(request, 'results.html', {
        'search_term': search_term,
        'errors': errors,
    })


def handle_keywords(keywords):
    if (
        keywords.startswith('"') and keywords.endswith('"')) or (
            keywords.startswith("'") and keywords.endswith("'")):
        return [keywords[1:-1]]
    return set(t for t in keywords.split(" ") if len(t) >= 3)


class LatestEntries(Feed):
    title = "TestLab"
    link = "/feed/"
    description = "Tester's Laboratory"

    def items(self):
        return Post.objects.filter(published=True).order_by('-created')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    def item_link(self, item):
        return reverse('post', args=[item.slug])
