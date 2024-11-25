from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lecturers/', views.lecturers_list, name='lecturers_list'),
    path('subjects/', views.subjects_list, name='subjects_list'),
    path('halls/', views.halls_list, name='halls_list'),
]