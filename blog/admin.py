from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post) # права администратора
admin.site.register(Comment)