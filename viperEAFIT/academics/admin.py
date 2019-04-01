from django.contrib import admin
from academics.models import Program, SubProgram, Course

# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    list_per_page = 25 
    search_fields = ('name', )


@admin.register(SubProgram)
class SubProgramAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name', )
    list_per_page = 25
    search_fields = ('name', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'subprogram', 'is_active', )
    list_display_links = ('name', )
    list_per_page = 25 
    search_fields = ('name', 'program', )


