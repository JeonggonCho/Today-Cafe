from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Post, Comment, Emote, PostPhoto
from .forms import PostForm, CommentForm, ReCommentForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def index(request):
    posts = Post.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page)
    context = {
        'posts': page_obj,
    }
    return render(request, 'posts/posts.html', context)


EMOTIONS = [
    {'label': '재밌어요', 'value': 1},
    {'label': '싫어요', 'value': 2},
    {'label': '화나요', 'value': 3},
]


def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    emotions = []
    for emotion in EMOTIONS:
        label = emotion['label']
        value = emotion['value']
        count = Emote.objects.filter(post=post, emotion=value).count()
        if request.user.is_authenticated:
            exist = Emote.objects.filter(post=post, emotion=value, user=request.user)
        else:
            exist = None
        emotions.append(
            {
            'label': label,
            'value': value,
            'count': count,
            'exist': exist,
            }
        )
    comments = post.comment_set.all()

    photos = PostPhoto.objects.filter(post_id=post_pk)


    comment_form = CommentForm()
    recommnet_form = ReCommentForm()
    context = {
        'emotions': emotions,
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
        'recommnet_form' : recommnet_form,
        'photos' : photos,

    }
    return render(request, 'posts/detail.html', context)


@login_required
def emotes(request, post_pk, emotion):
    post = Post.objects.get(pk=post_pk)
    filter_query = Emote.objects.filter(
        post=post,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(post=post, user=request.user, emotion=emotion)

    return redirect('posts:detail', post_pk)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            images = request.FILES.getlist('image')
            for image in images:
                photos = PostPhoto(post=post, photo=image)
                photos.save()
            return redirect('posts:detail', post.pk)
    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'posts/create.html', context)


@login_required
def update(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('posts:detail', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:index')
    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'posts/update.html', context)


@login_required
def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.user == post.user:
        post.delete()
    return redirect('posts:index')


@login_required
def comments_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.post = post
        comment.user = request.user
        comment.save()
        return redirect('posts:detail', post.pk)
    context = {
        'post': post,
        'comment_form': comment_form,
    }
    return render(request, 'posts/detail.html', context)


@login_required
def recomment(request, post_pk):
    comment_id = request.POST.get('comment_id')
    recomment_form = ReCommentForm(request.POST)
    if recomment_form.is_valid() and comment_id:
        recomment = recomment_form.save(commit=False)
        recomment.comment_id = comment_id
        recomment.save()
    return redirect('posts:detail', post_pk)



@login_required
def comments_delete(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('posts:detail', post_pk)


@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        request.user.like_posts.remove(post)
    else:
        post.like_users.add(request.user)
    return redirect('posts:detail', post_pk)


@login_required
def comment_likes(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    return redirect('posts:detail', post_pk)


def search(request):
    query = None
    search_list = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        search_list = Post.objects.filter(
            Q(title__icontains=query) # 제목 검색
        ).distinct() # 검색 결과 중복 제거
    context = {
        'query': query,
        'search_list': search_list,
    }
    return render(request, 'posts/search.html', context)
