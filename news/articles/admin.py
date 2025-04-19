from django.contrib import admin
from .models import Article, Comment

# Register your models here.
class CommentInline(admin.TabularInline): # new
    model = Comment 

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["id","author", "date", "title", "body",]
    inlines = [CommentInline]

class CommentAdmin(admin.ModelAdmin):
    list_display = ["id","date", "author", "article", "comment"]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment,CommentAdmin)
