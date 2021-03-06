from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models import User, Teacher
from schedules.models import Schedule

class UpdateTeacherVenueForm(forms.ModelForm):

    class Meta:
        model = Teacher
        fields = ['venues']
        widgets = {
            'venues' : forms.CheckboxSelectMultiple()
        }
        labels = {
            'venues': ''
        }


class TeacherScheduleForm(forms.ModelForm):
    TIME_CHOICES = (
        ('6:00 - 7:00'),
        ('7:00 - 8:00'),
        ('8:00 - 9:00'),
        ('9:00 - 10:00'),
        ('10:00 - 11:00'),
        ('11:00 - 12:00'),
        ('12:00 - 13:00'),
        ('13:00 - 14:00'),
        ('14:00 - 15:00'),
        ('15:00 - 16:00'),
        ('16:00 - 17:00'),
        ('17:00 - 18:00'),
        ('18:00 - 19:00'),
        ('19:00 - 20:00'),
        ('20:00 - 21:00')
    )
    class Meta:
        model = Schedule
        fields = ['monday', 'tuesday', 'wednesday',
                  'thursday', 'friday', 'saturday']
        labels = {
            'monday': '', 'tuesday': '', 'wednesday': '', 'thursday': '', 'friday': '', 'saturday': ''
        }


class TeacherScheduleCreateForm(forms.ModelForm):
    TIME_CHOICES = (
        ('6:00 - 7:00'),
        ('7:00 - 8:00'),
        ('8:00 - 9:00'),
        ('9:00 - 10:00'),
        ('10:00 - 11:00'),
        ('11:00 - 12:00'),
        ('12:00 - 13:00'),
        ('13:00 - 14:00'),
        ('14:00 - 15:00'),
        ('15:00 - 16:00'),
        ('16:00 - 17:00'),
        ('17:00 - 18:00'),
        ('18:00 - 19:00'),
        ('19:00 - 20:00'),
        ('20:00 - 21:00')
    )
    class Meta:
        model = Schedule
        fields = ['name', 'monday', 'tuesday',
                  'wednesday', 'thursday', 'friday', 'saturday']
        widgets = {
            'name': forms.HiddenInput(attrs={'name': 'name', 'id': 'name'})
        }
        labels = {
            'name': '', 'monday': '', 'tuesday': '', 'wednesday': '', 'thursday': '', 'friday': '', 'saturday': ''
        }




# class TeacherCreationForm(UserCreationForm):
#     pass
#     # user = forms.InlineForeignKeyField(User)
#     # # identification = forms.IntegerField()
#     # status = forms.ChoiceField(choices=Teacher.STATUS_CHOICES)
#     # subprograms = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
#     # courses = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)

#     # # Red Flags
#     # sufficiency = forms.BooleanField()
#     # simevi = forms.BooleanField()

#     # # Gold Stars
#     # coor_eval = forms.IntegerField()
#     # student_eval = forms.IntegerField()
#     # auto_eval = forms.IntegerField()
#     # observations = forms.IntegerField()
#     # pcp = forms.IntegerField()

#     # class Meta:
#     #     model = Teacher
#     #     fields = [
#     #         'user',
#     #         'identification',
#     #         'status',
#     #         'subprograms',
#     #         'courses',
#     #         'sufficiency',
#     #         'simevi',
#     #         'coor_eval',
#     #         'student_eval',
#     #         'auto_eval',
#     #         'observations',
#     #         'pcp',
#     #     ]

#     class Meta(UserCreationForm.Meta):
#         model = User
#         # fields = [
#         #     'first_name',
#         #     'last_name',
#         #     'email',
#         #     'username',
#         #     'password1',
#         #     'password2'
#         # ]

#     # Make sure operations are done in a single database transaction
#     # and avoid data inconsistencies in case of error
#     @transaction.atomic
#     def save(self, commit=True):
#         user = super().save(commit=False) # Returns the user model without committing to db
#         user.user_type = 'TC' # Set teacher value
#         user.save() # Saves the user
#         # Creates the teacher object and links it to the created user
#         Teacher.objects.create(
#             user=user,
#             identification=self.cleaned_data.get('identification'),
#             status=self.cleaned_data.get('status'),
#         )
#         return user        


# class TeacherCreationForm2(UserCreationForm):
#     first_name = forms.CharField(
#         label='Nombre',
#         max_length=20
#     )
#     last_name = forms.CharField(
#         label='Apellido',
#         max_length=20
#     )
#     identification = forms.IntegerField(
#         label='Número de Indentificación',
#     )
#     email = forms.EmailField()
#     status = forms.ChoiceField(
#         label='Estatus',
#         choices=Teacher.STATUS_CHOICES
#     )

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = [
#             'first_name',
#             'last_name',
#             'identification',
#             'email',
#             'status',
#             'username',
#             'password1',
#             'password2'
#         ]

#     # Make sure operations are done in a single database transaction
#     # and avoid data inconsistencies in case of error
#     @transaction.atomic
#     def save(self, commit=True):
#         user = super().save(commit=False) # Returns the user model without committing to db
#         user.user_type = 'TC' # Set teacher value
#         user.save() # Saves the user
#         # Creates the teacher object and links it to the created user
#         Teacher.objects.create(
#             user=user,
#             identification=self.cleaned_data.get('identification'),
#             status=self.cleaned_data.get('status'),
#         )
#         return user


