from django.db import models

from accounts.models import User


class Product(models.Model):
    STATUS_CHOICES = [
        ('activate', 'Activate'),
        ('noactivate', 'Noactivate')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User ID')
    name = models.CharField(max_length=200, verbose_name='Product name')
    photo = models.ImageField(upload_to='pics', blank=True, null=True, verbose_name='Photo')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='price')
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='activate', verbose_name='Status')

    def __str__(self):
        return self.name
