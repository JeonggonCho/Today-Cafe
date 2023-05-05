from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Post, Review, Comment, Emote, ReviewPhoto
from .forms import PostForm, CommentForm, ReviewForm, ReCommentForm
from django.core.paginator import Paginator
from django.db.models import Q


# Create your views here.
def posts(request):
    reviews = Review.objects.filter()
    posts = Post.objects.order_by('-pk')
    page = request.GET.get('page', '1')
    per_page = 5
    paginator = Paginator(posts, per_page)
    page_obj = paginator.get_page(page)
    context = {
        'posts': page_obj,
    }
    return render(request,'posts/posts.html', context)


EMOTIONS = [
    {'label': '재밌어요', 'value': 1},
    {'label': '싫어요', 'value': 2},
    {'label': '화나요', 'value': 3},
]


def post(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    reviews = Review.objects.filter(post_id=post_pk).order_by('-created_at')
    context = {
        'post': post,
        'reviews': reviews,
    }
    return render(request, 'posts/post.html', context)


@login_required
def emotes(request, review_pk, emotion):
    review = Review.objects.get(pk=review_pk)
    filter_query = Emote.objects.filter(
        review=review,
        user=request.user,
        emotion=emotion,
    )
    if filter_query.exists():
        filter_query.delete()
    else:
        Emote.objects.create(review=review, user=request.user, emotion=emotion)

    return redirect('posts:post', review_pk)


@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:post', post.pk)
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
                return redirect('posts:post', post.pk)
        else:
            form = PostForm(instance=post)
    else:
        return redirect('posts:posts')
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
    return redirect('posts:posts')


def review_detail(request, post_pk, review_pk):
    post = Post.objects.get(pk=post_pk)
    review = Review.objects.get(pk=review_pk)
    comments = review.comment_set.all()
    comment_form = CommentForm()
    photos = ReviewPhoto.objects.filter(review_id=review_pk)
    context = {
        'post':post,
        'review': review,
        'comments': comments,
        'comment_form': comment_form,
        'photos': photos,
    }
    return render(request, 'posts/review_detail.html', context)


@login_required
def review_create(request, post_pk):
    post = Post.objects.get(pk=post_pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.post = post
            review.user = request.user
            review.save()

            # 복수첨부된 이미지 리스트 저장
            images = request.FILES.getlist('image')
            for image in images:
                photo = ReviewPhoto(post=post, review=review, photo=image)
                photo.save()

            return redirect('posts:review_detail', post_pk=post.pk, review_pk=review.pk)
    else:
        review_form = ReviewForm()
    
    context = {
        'post': post,
        'review_form': review_form,
    }
    return render(request, 'posts/review_create.html', context)


@login_required
def review_update(request, post_pk, review_pk):
    post = Post.objects.get(pk=post_pk)
    review = Review.objects.get(post_id=post_pk, pk=review_pk)
    if request.user == review.user:
        if request.method == 'POST':
            review_form = ReviewForm(request.POST, request.FILES, instance=review)
            if review_form.is_valid():
                review_form.save()
                return redirect('posts:review_detail', post_pk=post.pk, review_pk=review.pk)
        else:
            review_form = ReviewForm(instance=review)
    else:
        return redirect('posts:review_detail', post_pk=post.pk, review_pk=review.pk)
    context = {
        'review_form': review_form,
        'post': post,
        'review': review,
    }
    return render(request, 'posts/review_update.html', context)


@login_required
def review_likes(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)

    if review.like_users.filter(pk=request.user.pk).exists():
        review.like_users.remove(request.user)
    else:
        review.like_users.add(request.user)
    return redirect('posts:review_detail', post_pk, review_pk)


@login_required
def review_delete(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.user == review.user:
        review.delete()
    return redirect('posts:post', post_pk)


@login_required
def comments_create(request, post_pk, review_pk):
    review = Review.objects.get(pk=review_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.review = review
        comment.user = request.user
        comment.save()
        return redirect('posts:review_detail', post_pk, review_pk)
    context = {
        'review': review,
        'comment_form': comment_form,
    }
    return render(request, 'posts/review_detail.html', context)



@login_required
def recomment(request, post_pk):
    comment_id = request.POST.get('comment_id')
    recomment_form = ReCommentForm(request.POST)
    if recomment_form.is_valid() and comment_id:
        recomment = recomment_form.save(commit=False)
        recomment.comment_id = comment_id
        recomment.save()
    return redirect('posts:post', post_pk)


@login_required
def comments_delete(request, post_pk, review_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if comment.user == request.user:
        comment.delete()
    return redirect('posts:review_detail', post_pk, review_pk)


@login_required
def likes(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.like_users.filter(pk=request.user.pk).exists():
        request.user.like_posts.remove(post)
    else:
        post.like_users.add(request.user)
    return redirect('posts:post', post_pk)


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
