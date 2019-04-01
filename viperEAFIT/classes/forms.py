from django import forms
from classes.models import Class
from academics.models import Course, SubProgram
from venues.models import Venue
from accounts.models import Teacher, Coordinator
from schedules.models import Schedule
from schedules.forms import SetScheduleForm
from django.forms.models import inlineformset_factory


# ScheduleFormSet = inlineformset_factory(models.)
class CreateClassForm(forms.ModelForm):
    subprogram = forms.ModelChoiceField(
        label='Sub-Program',
        queryset=SubProgram.objects.all()
    )
    # schedule = SetScheduleForm()

    class Meta:
        model = Class
        fields = ['subprogram', 'course', 'intensity', 'venue', 'teacher', 'schedule', 'start_date']


    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user', None)
        
        # Fetch the coordinator's subprograms
        subprogram_qs = SubProgram.objects.filter( 
            program=Coordinator.objects.filter(user=self.user.id).values_list('program', flat=True)[0]
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
                teacher_id = int(self.data.get('teacher'))
                self.fields['teacher'].queryset = Teacher.objects.filter(id=teacher_id).order_by('name')
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['teacher'].queryset = self.instance.teacher.teacher_set.order_by('name')

        # Previous code is not needed for intensity since it is a char based field
        # 














class CreateClassForm2(forms.ModelForm):
    # subprogram = forms.ModelChoiceField(
    #     label='Sub-Program',
    #     # queryset=SubProgram.objects.all()
    #     queryset=SubProgram.objects.filter(
    #         program=Coordinator.objects.filter(user=self.user.id).values_list('program', flat=True)[0]
    #     )
    # )
    subprogram = forms.ModelChoiceField(
        label='Sub-Program',
        queryset=SubProgram.objects.none()
    )
    # course = forms.ModelMultipleChoiceField(
    #     queryset=Course.objects.filter(subprogram='Ingles Adultos'),
    # )
    # intensity = forms.ChoiceField(
    #     choices=Class.INTENSITY_CHOICES
    # )
    # venue = forms.ModelChoiceField(
    #     queryset=Venue.objects.all()
    # )
    # teacher = forms.ModelChoiceField(
    #     queryset=Teacher.objects.all()
    # )
    # schedule = forms.ModelChoiceField(
    #     queryset=Schedule.objects.all()
    # ) # Mirar bien como hacerlo
    # start_date = forms.DateField(
    #     label='Start Date (YYYY-MM-DD)'
    # )

    class Meta:
        model = Class
        fields = ['subprogram', 'course', 'intensity', 'venue', 'teacher', 'schedule', 'start_date']


    def __init__(self, *args, **kwargs):
        if kwargs.get('user'):
            self.user = kwargs.pop('user', None)
        # subprogram_qs = SubProgram.objects.filter(
        #     program=Coordinator.objects.filter(user=self.user.id).values_list('program', flat=True)[0]
        # )
        super(CreateClassForm2, self).__init__(*args, **kwargs)
        # self.fields['subprogram'].queryset = subprogram_qs

    # def __init__(self, *args, **kwargs):
    #     print(kwargs)
    #     if kwargs.get('user'):
    #         self.user = kwargs.pop('user', None)
    #         print(self.user.first_name, self.user.user_type)
    #         coor_profile = Coordinator.objects.filter(user=self.user.id)
    #         # print(coor_profile)
    #         print(coor_profile.values_list('program', flat=True)[0])
    #         # print(coor_profile.values('program')[0].get('program'))
    #     super(CreateClassForm, self).__init__(*args, **kwargs)

    # def __init__(self, *args, **kwargs):
    #     print(kwargs)
    # #     # course_qs = kwargs.pop('subprogram')
    #     super(CreateClassForm, self).__init__(*args, **kwargs)
    # #     # self.fields['course'].queryset = course_qs