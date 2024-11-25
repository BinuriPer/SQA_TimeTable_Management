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

from django.shortcuts import render, redirect
from .models import Timetable
from django.contrib.auth.decorators import login_required

@login_required
def manage_timetable(request):
    if not request.user.is_admin:
        return redirect('home')  # Redirect if not admin

    if request.method == 'POST':
        # Handle form submission to create or update timetable entries
        # Validate that the same lecturer, students, and hall are not assigned at the same time
        pass

    timetables = Timetable.objects.all()
    return render(request, 'manage_timetable.html', {'timetables': timetables})

@login_required
def request_leave(request):
    if request.method == 'POST':
        # Handle leave request and assign a substitute
        pass
    return render(request, 'request_leave.html')


def allocate_time(lecturer):
    if lecturer.position == 'Lecturer (Probationary)':
        return 20  
    if lecturer.position == 'Senior Lecturer – Grade I':
        return 20 
    if lecturer.position == 'Professor':
        return 20 
    if lecturer.position == 'Temporary Assistant Lecturer':
        return 20 