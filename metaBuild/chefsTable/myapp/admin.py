from django.contrib import admin
from .models import Menu, MenuCategory
from .models import Personel, Working_Station, Shifts

# Register your models here.

#Defining the model admin class and list_display for viewing contents as a table
class MenuAdmin(admin.ModelAdmin):
    list_display = ("category_id", "menu_item", "price")

class MenucategoryAdmin(admin.ModelAdmin):
    list_display = ("menu_category_name")

class PersonelAdmin(admin.ModelAdmin):
    list_display = ("full_name", "phone_number","availability","age", "sex","duty_station", "shift")

class Working_StationAdmin(admin.ModelAdmin):
    list_display = ("working_area")

class ShiftsAdmin(admin.ModelAdmin):
    list_display = ("time_allocated", "time_in", "time_out")

# Registering both the Model and Its Admin View for tabular Viewing at the Admin Site
admin.site.register(MenuCategory)
admin.site.register(Menu,MenuAdmin)
admin.site.register(Personel, PersonelAdmin)
admin.site.register(Working_Station)
admin.site.register(Shifts,ShiftsAdmin)

