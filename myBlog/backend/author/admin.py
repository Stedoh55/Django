from django.contrib import admin
from .models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'bio')

admin.site.register(Author,AuthorAdmin)
