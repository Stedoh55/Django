from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","author", "date", "title", "body",]

admin.site.register(Article, ArticleAdmin)
