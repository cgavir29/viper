from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from accounts.models import User, Coordinator, Teacher


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ('username', 'first_name',
                    'last_name', 'email', 'user_type')
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
    list_display = ('id', 'user', 'identification', 'user_first_name',
                    'user_last_name', 'user_email',)
    list_display_links = ('user', )
    search_fields = ('user__first_name', 'identification', 'user__last_name', 'user__email',)

    fieldsets = (
        (('General Information'), {
         'fields': ('user', 'identification', 'status',)}),
        (('Red Flags'), {'fields': ('sufficiency', 'simevi',)}),
        (('Gold Stars'), {'fields': (
            'coor_eval', 'student_eval', 'auto_eval', 'observations', 'pcp',
        )})
    )
    # filter_horizontal = ('courses', 'subprograms')
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


admin.site.index_title = None
admin.site.unregister(Group)
