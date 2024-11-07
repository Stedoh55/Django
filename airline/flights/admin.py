from django.contrib import admin
from .models import Flights, Airport

# Register your models here.
class FlightsAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class AirportAdmin(admin.ModelAdmin):
    list_display = ("id", "city", "code")

admin.site.register(Flights, FlightsAdmin)
admin.site.register(Airport, AirportAdmin)