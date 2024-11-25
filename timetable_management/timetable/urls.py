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
