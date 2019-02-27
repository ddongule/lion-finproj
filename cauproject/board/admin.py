from django.contrib import admin
from .models import Post,Notice, Comment
# Register your models here.

admin.site.register(Post)
admin.site.register(Notice)
admin.site.register(Comment)