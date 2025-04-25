from django.contrib import admin
from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author','created_at', 'title', 'body','updated_at')

admin.site.register(Post, PostAdmin)
