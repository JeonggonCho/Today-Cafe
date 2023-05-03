from django.db import models
import os
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from django.conf import settings

# Create your models here.
class Profile(models.Model):
    image = models.ImageField(blank=True, upload_to='images/profile/')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 80}
    )


class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts')
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images/post/%Y/%m/%d/')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.CharField(max_length=200)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class PostPhoto(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='posts/photos/')
    
    def __str__(self):
        return self.content
    


class Emote(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    emotion = models.CharField(max_length=10)


class ReComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    content = models.CharField('대댓글', max_length=150)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.content
