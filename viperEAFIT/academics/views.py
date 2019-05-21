from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.views import generic
from accounts.models import User, Teacher
from schedules.models import Schedule
from .models import Program, SubProgram, Course, Class
from .forms import CreateClassForm, UpdateClassForm
from django.http import HttpResponseRedirect


class CreateClassView(LoginRequiredMixin, generic.CreateView):
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
    teachers = Course.objects.get(id=course).teachers.all()
    # print(teachers)
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


class ClassUpdateView(LoginRequiredMixin, generic.UpdateView):
    login_url = ''
    redirect_field_name = 'login'
    template_name = 'academics/class_update.html'
    model = Class
    form_class = UpdateClassForm

    # def get_form_kwargs(self):
    #     '''This goes in the Update view'''
    #     kwargs = super(ClassUpdateView, self).get_form_kwargs()
    #     user = self.request.user
    #     if user:
    #         kwargs['user'] = user

    #     return kwargs
    # def get_object(self):
    #     print(self.request.POST.get('pk'))
    #     print(Class.objects.get(id=self.request.GET.get('pk')))
    #     current_class = get_object_or_404(Class, pk=self.request.GET.get('pk'))
    #     return current_class
    

class CoordinatorClassListView(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'academics/class_list.html'
    success_url = reverse_lazy('academics:class_list')

    def post(self, request, *args, **kwargs):
        if 'id' in request.POST:
            class_id = request.POST.get('id')
            current_class = Class.objects.get(id=class_id)
            current_class.delete()

        return redirect(self.success_url)


    def get_queryset(self):
        program = Program.objects.get(coor=self.request.user)
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

