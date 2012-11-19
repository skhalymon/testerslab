from django.shortcuts import render, get_object_or_404
from blog.models import Post


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

def category(request, cat):
    posts = Post.objects.filter(categories__name=cat)
    context = {
        'posts': posts,
        'cat': cat,
    }
    return render(request, 'category.html', context)

def archive(request):
    all_posts = Post.objects.filter(published=True).order_by('-created')
    context = {
        'all_posts': all_posts,
    }
    return render(request, 'archive.html', context)
