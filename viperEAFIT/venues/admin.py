from django.contrib import admin
from .models import Venue

# Register your models here.
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'email')
    list_display_links = ('name', )
    list_per_page = 25 # Max listings per page
    search_fields = ('name', )
