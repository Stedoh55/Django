from django.contrib import admin
from .models import Menu
from .models import MenuCategory

# Register your models here.
admin.site.register(Menu)
admin.site.register(MenuCategory)
