from django.contrib import admin
from .models import Schedule

# Register your models here.
@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('name', 'intensity', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')
    list_display_links = ('name', )
    list_per_page = 25 # Max listings per page
    search_fields = ('id', 'name')