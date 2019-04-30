from django.urls import path

from .views import (
        LoginView,
        LogoutView,
        CoordinatorDashboardView,
        TeacherDashboardView,
        TeacherListView,
        ClassListView,
        TeacherDetailView,
)

app_name = 'accounts'
urlpatterns = [
        path('', LoginView.as_view(), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('coordinator/', CoordinatorDashboardView.as_view(), name='coordinator'),
        path('teacher/', TeacherDashboardView.as_view(), name='teacher'),
        path('teacher/detail/', TeacherDetailView.as_view(), name='teacher_detail'),
        path('teacher/class_list', ClassListView.as_view(), name='class_list'),
        path('coordinator/teacher_list/', TeacherListView.as_view(), name='teacher_list'),
]