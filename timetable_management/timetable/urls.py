from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lecturers/', views.lecturers_list, name='lecturers'),
    path('subjects/', views.subjects_list, name='subjects'),  
    path('halls/', views.halls_list, name='halls'),
    path('manage-timetable/', views.manage_timetable, name='manage_timetable'),
    path('request-leave/', views.request_leave, name='request_leave'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]

from django.urls import path
from .views import LecturerListView, SubjectListView, TimeSlotListView, CreateTimeSlotView

urlpatterns = [
    path('lecturers/', LecturerListView.as_view(), name='lecturer_list'),
    path('subjects/', SubjectListView.as_view(), name='subject_list'),
    path('timeslots/', TimeSlotListView.as_view(), name='timeslot_list'),
    path('timeslots/create/', CreateTimeSlotView.as_view(), name='create_timeslot'),
]