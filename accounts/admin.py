from django.contrib import admin

from accounts.views import User
from main.models import Product


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

