from django.contrib import admin
from classes.models import Class

# Register your models here.
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'intensity', 'venue', 'teacher', 'schedule')
    list_display_links = ('id', )
    list_per_page = 25 # Max listings per page
    search_fields = ('id', 'course', 'intensity', 'venue', 'teacher', 'schedule')