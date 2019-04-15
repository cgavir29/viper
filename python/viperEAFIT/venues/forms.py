from django import forms
from .models import Venue

class SetVenuesForm(forms.ModelForm):
    venues = forms.ModelMultipleChoiceField(
        queryset=Venue.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Venue
        fields = ['venues']