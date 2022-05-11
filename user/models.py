from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, date


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    bio = models.CharField(max_length=200, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.username

    @property
    def age(self):
        return date.today().year - self.birthday.year



