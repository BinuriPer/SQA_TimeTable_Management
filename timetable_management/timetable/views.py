from django.shortcuts import render

from .models import Lecturer, Subject, Hall, TimeSlot

def index(request):
    time_slots = TimeSlot.objects.all()
    return render(request, 'timetable/index.html', {'time_slots': time_slots})

def lecturers_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'timetable/lecturers.html', {'lecturers': lecturers})

def subjects_list(request):
    subjects = Subject.objects.all()
    return render(request, 'timetable/subjects.html', {'subjects': subjects})

def halls_list(request):
    halls = Hall.objects.all()
    return render(request, 'timetable/halls.html', {'halls': halls})