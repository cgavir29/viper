from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from classes.forms import CreateClassForm
from .models import Class
from academics.models import Course
from accounts.models import Teacher
from schedules.models import Schedule

# Create your views here.
class CreateClassView(CreateView):
    model = Class
    form_class = CreateClassForm
    success_url = reverse_lazy('accounts:coordinator')

    def get_form_kwargs(self):
        '''This goes in the Update view'''
        kwargs = super(CreateClassView, self).get_form_kwargs()
        user = self.request.user
        if user:
            kwargs['user'] = user
        return kwargs


def load_courses(request):
    subprogram = request.GET.get('subprogram')
    # print(subprogram)
    courses = Course.objects.filter(subprogram=subprogram).order_by('name')
    context = {
        'courses': courses
    }
    return render(request, 'classes/course_dropdown_options.html', context)


def load_teachers(request):
    course = request.GET.get('course')
    venue = request.GET.get('venue')
    print(venue)
    teachers = Teacher.objects.filter(courses=course)
    # print(teachers[0].user.username)
    context = {
        'teachers': teachers
    }
    return render(request, 'classes/teacher_dropdown_options.html', context)


def load_schedules(request):
    intensity = request.GET.get('intensity')
    schedules = Schedule.objects.filter(intensity=intensity)
    context = {
        'schedules': schedules
    }
    return render(request, 'classes/schedule_dropdown_options.html', context)
