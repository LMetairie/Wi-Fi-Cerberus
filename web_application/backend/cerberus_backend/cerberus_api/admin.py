from django.contrib import admin
from .models import DetectedDevices

# Register your models here.
class DetectedDevicesAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'mac_address', 'signal_strength', 'lat', 'lon')
    list_links = ('id', 'mac_address')
    search_fields = ('mac_address', 'id')
    list_per_page = 25

admin.site.register(DetectedDevices, DetectedDevicesAdmin)