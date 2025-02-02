from django.contrib import admin
from .models import MenuItem, Category

# Register your models here.
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('id','category', 'title', 'price', 'inventory')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title')

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category, CategoryAdmin)
