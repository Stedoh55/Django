from django.contrib import admin
from .models import MenuItem, Category, UserComment

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title', 'price', 'inventory')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')

class UserCommentAdmin(admin.ModelAdmin):
    list_display = ('time_log', 'first_name', 'last_name','comment')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(UserComment, UserCommentAdmin)
