from django import forms
from .models import Schedule

class SetScheduleForm(forms.ModelForm):
    monday = forms.MultipleChoiceField(choices=Schedule.TIME_CHOICES, widget=forms.CheckboxSelectMultiple)
    tuesday = forms.MultipleChoiceField(choices=Schedule.TIME_CHOICES, widget=forms.CheckboxSelectMultiple)
    wednesday = forms.MultipleChoiceField(choices=Schedule.TIME_CHOICES, widget=forms.CheckboxSelectMultiple)
    thursday = forms.MultipleChoiceField(choices=Schedule.TIME_CHOICES, widget=forms.CheckboxSelectMultiple)
    friday = forms.MultipleChoiceField(choices=Schedule.TIME_CHOICES, widget=forms.CheckboxSelectMultiple)
    saturday = forms.MultipleChoiceField(choices=Schedule.TIME_CHOICES, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Schedule
        fields = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']