from django.db import models
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
    address = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30, blank=True)
    menu = models.CharField(max_length=200)
    hours = models.CharField(max_length=30)
    information = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to='images/post/%Y/%m/%d/')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

   




class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    image = models.ImageField(blank=True, null=True, upload_to='images/review/%Y/%m/%d/')
    content = models.CharField(max_length=200)
    rating = models.FloatField(verbose_name='평점')
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def star_rating(self):
        rounded_rating = round(self.rating * 2) / 2
        return '★' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
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
