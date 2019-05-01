from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from accounts.models import User, Coordinator, Teacher

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

# class CoordinatorCreationForm(UserCreationForm):
#     first_name = forms.CharField(
#         label='Nombre',
#         max_length=20
#         )
#     last_name = forms.CharField(
#         label='Apellido',
#         max_length=20
#     )
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         # Fields to be displayed in the form, in that order
#         fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_coordinator = True
#         if commit:
#             user.save()
#         return user




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


