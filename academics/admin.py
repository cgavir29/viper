from django.contrib import admin
from academics.models import Program, SubProgram, Course, Class

# Register your models here.
@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'coor')
    list_display_links = ('name', )
    list_per_page = 25
    search_fields = ('name', 'coor')


@admin.register(SubProgram)
class SubProgramAdmin(admin.ModelAdmin):
    list_display = ('name', 'program')
    list_display_links = ('name', )
    list_per_page = 25
    search_fields = ('name', 'program__name')
    filter_horizontal = ('teachers', )


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'subprogram', 'is_active', )
    list_display_links = ('id', 'name', )
    list_per_page = 25
    search_fields = ('name', 'subprogram__name')
    filter_horizontal = ('teachers', )


@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'intensity', 'venue', 'schedule', 'teacher',)
    list_display_links = ('id', )
    list_per_page = 25
    search_fields = ('id', 'course', 'intensity', 'venue', 'teacher', 'schedule')
