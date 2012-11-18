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
