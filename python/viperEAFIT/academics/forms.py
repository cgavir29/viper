from django import forms
from venues.models import Venue
from accounts.models import Teacher, Coordinator
from schedules.models import Schedule
from schedules.forms import SetScheduleForm
from .models import Program, SubProgram, Course, Class


class CreateClassForm(forms.ModelForm):
    subprogram = forms.ModelChoiceField(queryset=SubProgram.objects.none())

    class Meta:
        model = Class
        fields = ['subprogram', 'course', 'intensity', 'venue', 'teacher', 'schedule', 'end_date']

    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user', None)
        
        subprogram_qs = SubProgram.objects.filter(
            program=Program.objects.get(coordinator=Coordinator.objects.get(user=self.user.id))
        )
        super().__init__(*args, **kwargs)
        self.fields['subprogram'].queryset = subprogram_qs
        self.fields['course'].queryset = Course.objects.none()
        self.fields['teacher'].queryset = Teacher.objects.none()

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['course'].queryset = Course.objects.filter(id=course_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Course queryset
        # elif self.instance.pk:
        #     self.fields['course'].queryset = self.instance.course.course_set.order_by('name')

        if 'teacher' in self.data:
            try:
                course_id = int(self.data.get('course'))
                teacher_id = int(self.data.get('teacher'))
                self.fields['teacher'].queryset = Teacher.objects.filter(id=teacher_id).order_by('name')
                #self.fields['teacher'].queryset = Course.objects.filter(teachers__in=course_id).order_by('name')
            except (ValueError, TypeError):
                pass
        #elif self.instance.pk:
        #    self.fields['teacher'].queryset = self.instance.teacher.teacher_set.order_by('name')

        # Previous code is not needed for intensity since it is a char based field
        # 
