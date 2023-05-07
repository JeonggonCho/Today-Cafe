from django.db import models
import os
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail
from django.conf import settings
from django.utils import timezone
from datetime import timedelta,datetime
from taggit.managers import TaggableManager

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
    category = models.CharField(max_length=10)
    image = models.ImageField(blank=True, null=True, upload_to='images/post/%Y/%m/%d/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = TaggableManager(blank=True)


    def str(self):
        return self.title
    
    def count_likes_user(self):
        return self.like_users.count()

    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(self.image)))
        super(Post, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_post = Post.objects.get(id=self.id)
            if self.image != old_post.image:
                if old_post.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, str(old_post.image.path)))
        super(Post, self).save(*args, **kwargs)

    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')
    image = models.ImageField(blank=True, null=True, upload_to='images/review/%Y/%m/%d/')
    content = models.CharField(max_length=200)
    rating = models.FloatField(verbose_name='평점')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def star_rating(self):
        rounded_rating = round(self.rating * 2) / 2
        return '⭐' * int(rounded_rating) + '☆' * (rounded_rating % 1 == 0.5)
    
    def count_likes_user(self):
        return self.like_users.count()
    
    def delete(self, *args, **kargs):
        if self.image:
            os.remove(os.path.join(settings.MEDIA_ROOT, str(self.image)))
        super(Review, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_review = Review.objects.get(id=self.id)
            if self.image != old_review.image:
                if old_review.image:
                    os.remove(os.path.join(settings.MEDIA_ROOT, str(old_review.image.path)))
        super(Review, self).save(*args, **kwargs)

    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False


class Comment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comments')
    content = models.CharField(max_length=200)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def count_likes_user(self):
        return self.like_users.count()
    
    @property
    def created_string(self):
        if self.created_at is None:
            return False

        time = datetime.now(tz=timezone.utc) - self.created_at

        if time < timedelta(minutes=1):
            return '방금 전'
        elif time < timedelta(hours=1):
            return str(int(time.seconds / 60)) + '분 전'
        elif time < timedelta(days=1):
            return str(int(time.seconds / 3600)) + '시간 전'
        elif time < timedelta(days=7):
            time = datetime.now(tz=timezone.utc).date() - self.created_at.date()
            return str(time.days) + '일 전'
        else:
            return False
    
    
class ReviewPhoto(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='reviews/photos/')
    
    def __str__(self):
        return self.content
    
    def delete(self, *args, **kargs):
        if self.photo:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.photo))
        super(ReviewPhoto, self).delete(*args, **kargs)

    def save(self, *args, **kwargs):
        if self.id:
            old_reviewPhoto = ReviewPhoto.objects.get(id=self.id)
            if self.photo != old_reviewPhoto.photo:
                if old_reviewPhoto.photo:
                    os.remove(os.path.join(settings.MEDIA_ROOT, old_reviewPhoto.photo.path))
        super(ReviewPhoto, self).save(*args, **kwargs)


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
