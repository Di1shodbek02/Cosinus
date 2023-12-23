from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, verbose_name='Phone Number')
    avatar = models.ImageField(upload_to='pics', blank=True, null=True, verbose_name='Avatar')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


