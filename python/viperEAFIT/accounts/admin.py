from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from accounts.models import User, Coordinator, Teacher


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'user_type')
    list_display_links = ('username', )
    list_per_page = 25
    search_fields = ('first_name', 'last_name', 'email', )
    add_fieldsets = (
        (None, {
            'fields': (
                'first_name', 'last_name', 'email', 'username', 
                'password1', 'password2', 'user_type',
                )
            }
        ),
    )


@admin.register(Coordinator)
class CoordinatorAdmin(admin.ModelAdmin):
    list_display = ('user', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'identification')
    list_display_links = ('user', )
    fieldsets = (
        (('General Information'), {'fields': ('user', 'identification', 'status',)}),
        (('Red Flags'), {'fields': ('sufficiency', 'simevi',)}),
        (('Gold Stars'), {'fields': (
            'coor_eval', 'student_eval', 'auto_eval', 'observations', 'pcp',
        )})
    )
    # filter_horizontal = ('courses', 'subprograms')

admin.site.index_title = None
admin.site.unregister(Group)
