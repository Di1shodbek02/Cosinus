from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    phone_number = models.CharField(max_length=13)

    def __str__(self):
        return self.first_name + self.last_name
