from django import forms
from venues.models import Venue
from accounts.models import User, Teacher
from schedules.models import Schedule
from schedules.forms import SetScheduleForm
from .models import Program, SubProgram, Course, Class


class CreateClassForm(forms.ModelForm):
    subprogram = forms.ModelChoiceField(queryset=SubProgram.objects.none())

    class Meta:
        model = Class
        fields = ['subprogram', 'course', 'intensity', 'venue', 'schedule', 'end_date', 'teacher',]

    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user', None)
        
        subprogram_qs = SubProgram.objects.filter(
            program=Program.objects.get(coor=self.user.id)
        )
        super().__init__(*args, **kwargs)
        self.fields['subprogram'].queryset = subprogram_qs
        self.fields['course'].queryset = Course.objects.none()
        self.fields['teacher'].queryset = Teacher.objects.none()
        self.fields['schedule'].queryset = Schedule.objects.none()

        if 'subprogram' in self.data:
            try:
                subprogram_id = int(self.data.get('subprogram'))
                print(Course.objects.filter(subprogram=subprogram_id).order_by('name'))
                self.fields['course'].queryset = Course.objects.filter(subprogram=subprogram_id).order_by('name')
            except (ValueError, TypeError):
                pass

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['teacher'].queryset = Course.objects.get(id=course_id).teachers.all()
            except (ValueError, TypeError):
                pass

        if 'intensity' in self.data:
            try:
                intensity = self.data.get('intensity')
                self.fields['schedule'].queryset = Schedule.objects.filter(intensity=intensity)
            except (ValueError, TypeError):
                pass


class UpdateClassForm(forms.ModelForm):

    class Meta:
        model = Class
        fields = ['course', 'intensity', 'venue', 'schedule', 'end_date', 'teacher',]

