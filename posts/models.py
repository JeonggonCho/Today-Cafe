from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import Thumbnail


# Create your models here.
class Profile(models.Model):
    image = models.ImageField(blank=True, upload_to='images/')
    image_thumbnail = ImageSpecField(
        source='image',
        processors=[Thumbnail(200, 200)],
        format='JPEG',
        options={'quality': 80}
    )