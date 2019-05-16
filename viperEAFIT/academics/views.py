from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views.generic import CreateView, ListView
from accounts.models import User, Coordinator, Teacher
from schedules.models import Schedule
from .models import Program, SubProgram, Course, Class
from .forms import CreateClassForm


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
    courses = Course.objects.filter(subprogram=subprogram).order_by('name')
    context = {
        'courses': courses
    }

    return render(request, 'academics/course_dropdown_options.html', context)


def load_teachers(request):
    course = request.GET.get('course')
    # venue = request.GET.get('venue')
    teachers = Course.objects.filter(id=course).values_list('teachers').order_by('name')
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


class CoordinatorClassList(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'academics/class_list.html'

    def get_queryset(self):
        current_coordinator = Coordinator.objects.get(user=self.request.user)
        program = Program.objects.get(coordinator=current_coordinator)
        # program = Program.objects.get(coor=self.request.user)
        subprograms = SubProgram.objects.filter(program=program)
        class_queryset = Class.objects.none()
        for subprogram in subprograms:
            courses = Course.objects.filter(subprogram=subprogram)
            for course in courses:
                class_queryset = class_queryset | Class.objects.filter(course=course)

        if 'q' in self.request.GET:
            query = self.request.GET.get('q')
            class_queryset = class_queryset.filter(
                Q(course__subprogram__name__icontains=query) |
                Q(course__name__icontains=query) |
                Q(intensity__icontains=query) |
                Q(venue__name__icontains=query) |
                Q(schedule__name__icontains=query) |
                Q(teacher__user__first_name__icontains=query) | # Arreglar cuando son nombre y apellido
                Q(teacher__user__last_name__icontains=query)
            )

        return class_queryset


