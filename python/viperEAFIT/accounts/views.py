from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.views.generic import FormView, ListView, View, DetailView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from schedules.forms import SetScheduleForm
from venues.forms import SetVenuesForm
from academics.models import Class
from .models import Teacher, User
from .forms import UpdateTeacherVenueForm


class LoginView(FormView):
    """
        Provides the ability to login users to the platform
    """
    form_class = AuthenticationForm
    template_name = 'accounts/login.html'
    
    def form_valid(self, form):
        # If the AuthenticationForm succeeds, log in the user
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


class LogoutView(View):
    """
        Logs users out
    """
    def get(self, request):
        logout(request)
        return redirect('accounts:login')


class CoordinatorDashboardView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'login'
    
    def get(self, request):
        current_user = request.user
        context = {
            'current_user' : current_user,
        }
        return render(request, 'accounts/coordinator.html', context)


class TeacherDashboardView(LoginRequiredMixin, View):
    login_url = '/'
    redirect_field_name = 'login'
 
    def get(self, request):
        current_user = request.user
        venues_form = SetVenuesForm(request.POST)
        schedule_form = SetScheduleForm(request.POST)
        context = {
            'current_user' : current_user,
            'venues_form' : venues_form,
            'schedule_form' : schedule_form
        }
        return render(request, 'accounts/teacher.html', context)


class TeacherDetailView(LoginRequiredMixin, DetailView):
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
        current_teacher.available_hours = request.POST['ah']
        current_teacher.save()

        self.object = self.get_object()
        context = super(TeacherDetailView, self).get_context_data(**kwargs)

        return render(request, self.success_url, context)




class TeacherListView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'accounts/teacher_list.html'
    queryset = Teacher.objects.all() # Cambiar esto


class ClassListView(LoginRequiredMixin, ListView):
    login_url = '/'
    redirect_field_name = 'login'
    template_name = 'accounts/class_list.html'

    def get_queryset(self):
        current_teacher = Teacher.objects.get(user=self.request.user)
        return Class.objects.filter(teacher=current_teacher)


class TeacherVenueUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/'
    redirect_field_name = 'login'
    model = Teacher
    template_name = 'accounts/teacher_venue_update.html'
    form_class = UpdateTeacherVenueForm
    success_url = '/teacher/'
