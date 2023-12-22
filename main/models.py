from django.db import models

from accounts.models import User


class Product(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='pics')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.name
