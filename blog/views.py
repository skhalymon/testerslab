from django.shortcuts import render
from blog.models import Post


def index(request):
    latest_posts = Post.objects.filter(published=True).order_by('-created')[:5]
    context = {'latest_posts': latest_posts}
    return render(request, 'posts.html', context)
