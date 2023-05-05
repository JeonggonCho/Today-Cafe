from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    # post관련 url
    path('', views.posts, name='posts'),
    path('<int:post_pk>/', views.post, name='post'),
    path('create/', views.create, name='create'),
    path('<int:post_pk>/delete/', views.delete, name='delete'),
    path('<int:post_pk>/update/', views.update, name='update'),
    path('<int:post_pk>/likes/', views.likes, name='likes'),


    # review관련 url
    path('<int:post_pk>/reviews/<int:review_pk>/', views.review_detail, name='review_detail'),
    path('<int:post_pk>/reviews/', views.review_create , name='review_create'),
    path('<int:post_pk>/reviews/<int:review_pk>/update/', views.review_update, name='review_update'),
    path('<int:post_pk>/reviews/<int:review_pk>/delete/', views.review_delete, name='review_delete'),
    path('<int:post_pk>/reviews/<int:review_pk>/likes', views.review_likes, name='review_likes',),
    # path('<int:post_pk>/emotes/<int:emotion>/', views.emotes, name='emotes'),


    # comment관련 url
    path('<int:post_pk>/reviews/<int:review_pk>/comments/', views.comments_create, name='comments_create'),
    path('<int:post_pk>/reviews/<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),


    # 기타 url
    path('search/', views.search, name="search"),
    path('<int:post_pk>/recomment/', views.recomment, name='recomment'),
    ]





















