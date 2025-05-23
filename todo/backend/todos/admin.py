from django.contrib import admin
from .models import Todo

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id','create_time', 'title', 'body')

admin.site.register(Todo, TodoAdmin)