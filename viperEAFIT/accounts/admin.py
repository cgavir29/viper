from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from accounts.models import User, Coordinator, Teacher

# Register your models here.

# class UserCreationForm(forms.ModelForm):
#     """A forms for creating custom new users."""
#     # first_name = forms.CharField(label='Nombre', required=True)
#     # last_name = forms.CharField(label='Apellido', required=True)
#     # email = forms.EmailField(required=True)
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)
#     user_type = forms.ChoiceField(label='User Type', choices=User.USER_TYPE_CHOICES)

#     class Meta:
#         model = User
#         fields = ('password1', 'password2', 'user_type')
#         # fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'user_type')

class CoordinatorCreationForm(forms.ModelForm):
    
    class Meta:
        model = Coordinator
        fields = ['user', 'program']

@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    # add_form = UserCreationForm
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
class Coordinator(admin.ModelAdmin):
    list_display = ('user', 'program')


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'identification', 'status', )


admin.site.index_title = None
admin.site.unregister(Group)