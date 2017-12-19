from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import Post


admin.site.register(Post)