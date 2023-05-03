from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class User(AbstractUser):
    profile_image = models.ImageField(blank=True, null=True, upload_to='images/profile/')
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)

