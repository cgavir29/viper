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
        fields = ['subprogram', 'course', 'intensity', 'venue', 'teacher', 'schedule',]

    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user', None)
        
        # Fetch the coordinator's subprograms
        # programs = Program.objects.all()
        # current__coor = Coordinator.objects.filter(user=self.user.id)
        # print(programs[0].coordinator.id, current__coor[0].id)
        # program_qs = Program.objects.filter(coordinator_id=self.user.id)
        # print(program_qs)
        # subprogram_qs = SubProgram.objects.filter(
        #     program=Program.objects.filter(coordinator=Coordinator.objects.filter(user=self.user.id)[0])[0]
        # )
        # print(subprogram_qs)
        # TRY WITH GET LATER, MIGHT BE EASIER
        subprogram_qs = SubProgram.objects.filter(
            program=Program.objects.filter(coordinator=Coordinator.objects.filter(user=self.user.id)[0])[0]
        )
        super().__init__(*args, **kwargs)
        self.fields['subprogram'].queryset = subprogram_qs
        self.fields['course'].queryset = Course.objects.none()
        self.fields['teacher'].queryset = Teacher.objects.none()
        self.fields['schedule'].queryset = Teacher.objects.none()

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
                teacher_id = int(self.data.get('teacher'))
                self.fields['teacher'].queryset = Teacher.objects.filter(id=teacher_id)
            except (ValueError, TypeError):
                pass
        # elif self.instance.pk:
        #     self.fields['teacher'].queryset = self.instance.teacher.teacher_set.order_by('name')

        if 'schedule' in self.data:
            try:
                schedule_id = int(self.data.get('schedule'))
                self.fields['schedule'].queryset = Schedule.objects.filter(id=schedule_id)
            except (ValueError, TypeError):
                pass
        
        