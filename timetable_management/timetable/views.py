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
    
# customer account
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            print("Redirecting to login page...")
            return redirect('login')
        else:
            messages.error(request, 'Please correct the errors below.')
            print("Form is not valid:", form.errors)
    else:
        form = RegisterForm()
    return render(request, 'timetable/register.html', {'form': form})

# timetable_management/views.py
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a home page or dashboard
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'timetable/login.html')  # Corrected path

# timetable/views.py

from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Lecturer, Subject, TimeSlot, Hall
from .forms import TimeSlotForm  # Ensure you have this form defined

class LecturerListView(ListView):
    model = Lecturer
    template_name = 'timetable/lecturer_list.html'  # Adjust this path if necessary
    context_object_name = 'lecturers'  # This will be the variable name in the template

class SubjectListView(ListView):
    model = Subject
    template_name = 'timetable/subject_list.html'  # Adjust this path if necessary
    context_object_name = 'subjects'

class TimeSlotListView(ListView):
    model = TimeSlot
    template_name = 'timetable/timeslot_list.html'  # Adjust this path if necessary
    context_object_name = 'timeslots'

class CreateTimeSlotView(CreateView):
    model = TimeSlot
    form_class = TimeSlotForm  # Ensure you have this form defined
    template_name = 'timetable/create_timeslot.html'  # Adjust this path if necessary
    success_url = reverse_lazy('timeslot_list')  # Redirect after successful creation