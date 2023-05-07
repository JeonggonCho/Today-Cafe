from django.shortcuts import render, redirect
from posts.models import Post

def index(request):
    recent_posts = Post.objects.order_by('-created_at')[:8]
    if recent_posts:
        context = {'recent_posts': recent_posts}
    else:
        context = {}
    return render(request, 'index.html', context)