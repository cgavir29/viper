from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm
from schedules.forms import SetScheduleForm
from venues.forms import SetVenuesForm
from academics.models import Program, SubProgram, Class
from .models import User, Teacher
from .forms import UpdateTeacherVenueForm, TeacherScheduleForm, TeacherScheduleCreateForm
from venues.models import Venue
from schedules.models import Schedule

class LoginView(generic.FormView):
    """
        Provides the ability to login users to the platform
    """
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            user_type = request.user.user_type
            if user_type == 'TC':
                return redirect('accounts:teacher')
            elif user_type == 'CO':
                return redirect('accounts:coordinator')
            else:
                return redirect('admin:index')
        
        return self.render_to_response(self.get_context_data())

    def get_success_url(self):
        user = self.request.user
        user_type = user.user_type
        target_url = ''
        if user_type == 'TC':
            target_url = 'teacher'
        elif user_type == 'CO':
            target_url = 'coordinator'
        else:
            target_url = 'admin'

        return str(target_url)


class LogoutView(generic.View):
    """
        Logs users out
    """
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class CoordinatorDashboardView(LoginRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'login'

    def get(self, request):
        try:
            coor_program = Program.objects.get(coor=request.user.id)
        except ObjectDoesNotExist:
            coor_program = Program.objects.none()
        context = {
            'coor_program' : coor_program,
        }

        return render(request, 'accounts/coordinator.html', context)


class TeacherDashboardView(LoginRequiredMixin, generic.View):
    login_url = '/'
    redirect_field_name = 'login'
 
    def get(self, request):
        venues_form = SetVenuesForm(request.POST)
        schedule_form = SetScheduleForm(request.POST)
        context = {
            'venues_form' : venues_form,
            'schedule_form' : schedule_form
        }

        return render(request, 'accounts/teacher.html', context)


class TeacherDetailView(LoginRequiredMixin, generic.DetailView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'accounts/teacher_detail.html'
    success_url = 'accounts/teacher.html'
    model = Teacher

    def get_queryset(self):
        return Teacher.objects.filter(user=self.request.user)

    def post(self, request, *args, **kwargs):
        current_teacher = Teacher.objects.get(user=request.user)
        current_teacher.user.email = request.POST['email']
        current_teacher.user.save()
        current_teacher.available_hours = request.POST['ah']
        current_teacher.save()
        self.object = self.get_object()
        context = super(TeacherDetailView, self).get_context_data(**kwargs)
        return render(request, self.success_url, context)


class TeacherListView(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'accounts/teacher_list.html'

    def get_queryset(self):
        # current_coordinator = Coordinator.objects.get(user=self.request.user)
        # program = Program.objects.get(coordinator=current_coordinator)
        program = Program.objects.get(coor=self.request.user)
        subprograms = SubProgram.objects.filter(program=program)
        teacher_queryset = Teacher.objects.none()
        for subprogram in subprograms:
            teacher_queryset = teacher_queryset | subprogram.teachers.all()

        if 'q' in self.request.GET:
            query = self.request.GET.get('q')
            teacher_queryset = teacher_queryset.filter(
                Q(user__first_name__icontains=query) | # Arreglar cuando son nombre y apellido
                Q(user__last_name__icontains=query) |
                Q(user__email__icontains=query) |
                Q(status__icontains=query)
            )

        return teacher_queryset


class ClassListView(LoginRequiredMixin, generic.ListView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'accounts/class_list.html'

    def get_queryset(self):
        current_teacher = Teacher.objects.get(user=self.request.user)
        return Class.objects.filter(teacher=current_teacher)


class TeacherVenueUpdate(LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    redirect_field_name = 'login'
    model = Teacher
    template_name = 'accounts/teacher_venue_update.html'
    form_class = UpdateTeacherVenueForm
    success_url = '/teacher/'


class TeacherScheduleView(LoginRequiredMixin, generic.UpdateView):
    login_url = '/'
    redirect_field_name = 'login'
    model = Schedule
    template_name = 'accounts/teacher_schedule_update.html'
    form_class = TeacherScheduleForm
    success_url = '/teacher/'


class TeacherScheduleCreateView(LoginRequiredMixin, generic.CreateView):
    login_url = '/'
    redirect_field_name = 'login'
    model = Schedule
    template_name = 'accounts/teacher_schedule_create.html'
    form_class = TeacherScheduleCreateForm
    success_url = '/teacher/'
    

    def post(self, request, *args, **kwargs):
        form = TeacherScheduleCreateForm(request.POST)
        if form.is_valid():
            current_teacher = Teacher.objects.get(user=self.request.user)
            new_schedule = form
            new_schedule.save()
            new_schedule.name = current_teacher.id
            new_schedule.save()
            current_teacher.availability = new_schedule.instance
            current_teacher.save()

        return super().post(request, *args, **kwargs)