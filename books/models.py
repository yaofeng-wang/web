from PIL import Image
from django.db import models
from backend.settings import MEDIA_ROOT
from users.models import UserProfile
from django.urls import reverse
from django.conf import settings
from django_resized import ResizedImageField


class Book(models.Model):

    seller = models.ForeignKey(to=UserProfile,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,
                                decimal_places=2)
    # resize image only if it is larger than 300 x 400
    # a smaller version of original image
    thumbnail = ResizedImageField(
        size=[300, 400], upload_to='books', quality=75, force_format='JPEG')
    # original image
    image = models.ImageField(upload_to='books')

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return reverse('display_book', args=[self.id])
