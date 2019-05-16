from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from accounts.models import User, Teacher


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('epik_unique_number', 'username', 'first_name',
                    'last_name', 'email', 'user_type', )
    list_display_links = ('epik_unique_number', )
    list_per_page = 25
    search_fields = ('first_name', 'last_name', 'email', 'username', 'epik_unique_number')
    add_fieldsets = (
        (None, {
            'fields': (
                'first_name', 'last_name', 'email', 'epik_unique_number', 'username',
                'password1', 'password2', 'user_type',
            )
        }
        ),
    )


# @admin.register(Coordinator)
# class CoordinatorAdmin(admin.ModelAdmin):
#     list_display = ('user', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_epik_unique_number','user', 'user_first_name',
                    'user_last_name', 'user_email',)
    list_display_links = ('id', 'user_epik_unique_number', )
    search_fields = ('user__first_name', 'user__last_name', 'user__email', 'user__epik_unique_number')

    fieldsets = (
        (('General Information'), {
         'fields': ('user', 'status', 'venues', 'availability')}),
        (('Red Flags'), {'fields': ('sufficiency', 'simevi',)}),
        (('Gold Stars'), {'fields': (
            'coor_eval', 'student_eval', 'auto_eval', 'observations', 'pcp',
        )})
    )
    def user_first_name(self, obj):
        return obj.user.first_name
    user_first_name.short_description = "First Name"
    user_first_name.admin_order_field = "user__first_name"

    def user_last_name(self, obj):
        return obj.user.last_name
    user_last_name.short_description = "Last Name"
    user_last_name.admin_order_field = "user__last_name"

    def user_email(self, obj):
        return obj.user.email
    user_email.short_description = "Email"
    user_email.admin_order_field = "user__email"

    def user_epik_unique_number(self, obj):
        return obj.user.epik_unique_number
    user_epik_unique_number.short_description = 'Epik Unique Number'
    user_epik_unique_number.admin_order_field = 'user__epik_unique_number'



admin.site.index_title = None
admin.site.unregister(Group)
