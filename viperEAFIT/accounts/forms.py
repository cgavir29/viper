from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


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
#         model = MyUser
#         # Fields to be displayed in the form, in that order
#         fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.is_coordinator = True
#         if commit:
#             user.save()
#         return user


# class TeacherCreationForm(UserCreationForm):
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
    # my_programs = forms.ModelMultipleChoiceField(
    #     label='Programas',
    #     queryset=SubProgram.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    # class Meta(UserCreationForm.Meta):
    #     model = MyUser
    #     fields = [
    #         'first_name',
    #         'last_name',
    #         'identification',
    #         'email',
    #         'status',
    #         'username',
    #         'password1',
    #         'password2'
    #     ]

    # # Make sure operations are done in a single database transaction
    # # and avoid data inconsistencies in case of error
    # @transaction.atomic
    # def save(self, commit=True):
    #     user = super().save(commit=False) # Returns the user model without committing to db
    #     user.user_type = 'TC' # Set teacher value
    #     user.save() # Saves the user
    #     # Creates the teacher object and links it to the created user
    #     Teacher.objects.create(
    #         user=user,
    #         identification=self.cleaned_data.get('identification'),
    #         status=self.cleaned_data.get('status'),
    #     )
    #     return user


