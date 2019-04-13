from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from accounts.models import Teacher
from schedules.models import Schedule
from .models import Course, Class
from .forms import CreateClassForm


# Create your views here.
class CreateClassView(LoginRequiredMixin, CreateView):
    model = Class
    form_class = CreateClassForm
    login_url = '/'
    redirect_field_name = 'login'
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
    return render(request, 'academics/course_dropdown_options.html', context)


def load_teachers(request):
    course = request.GET.get('course')
    venue = request.GET.get('venue')
    print(venue)
    #teachers = Teacher.objects.filter(courses__in=course)
    teachers = Course.objects.filter(id=course).values_list('teachers').order_by('name')
    print(teachers, type(teachers))
    teachers2 = Teacher.objects.filter(teachers__in=teachers)
    print(teachers2)
    #teachers = Course.objects.filter(teachers__in=course)
    # print(teachers[0].user.username)
    context = {
        'teachers': teachers
    }
    return render(request, 'academics/teacher_dropdown_options.html', context)


def load_schedules(request):
    intensity = request.GET.get('intensity')
    schedules = Schedule.objects.filter(intensity=intensity)
    context = {
        'schedules': schedules
    }
    return render(request, 'academics/schedule_dropdown_options.html', context)
