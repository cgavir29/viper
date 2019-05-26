from django.urls import path
from .views import (
        CreateClassView,
        load_courses,
        load_teachers,
        load_schedules,
        CoordinatorClassListView,
        ClassUpdateView,
)

app_name = 'academics'
urlpatterns = [
        path('create_class/', CreateClassView.as_view(), name='create_class'),
        path('class_list/', CoordinatorClassListView.as_view(), name='class_list'),
        path('class/<int:pk>/', ClassUpdateView.as_view(), name='class_update'),
        # For Dropdowns
        path('ajax/load-courses/', load_courses, name='ajax_load_courses'),
        path('ajax/load-teachers/', load_teachers, name='ajax_load_teachers'),
        path('ajax/load-schedules/', load_schedules, name='ajax_load_schedules'),
        
]