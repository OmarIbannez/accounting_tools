from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='user/photos/', blank=True, null=True)

    def photo_url(self):
        if not self.photo or not hasattr(self.photo, 'url'):
            '''You need to add a deafault photo'''
            return '/static/img/default_photo.png'
        return self.photo.url

    def get_full_name(self):
        return u'{0} {1} {2}'.format(self.first_name,  self.middle_name, self.last_name)
