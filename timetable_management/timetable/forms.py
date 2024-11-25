# forms.py

from django import forms
from .models import TimeSlot  # Ensure this import is correct

class TimeSlotForm(forms.ModelForm):
    class Meta:
        model = TimeSlot
        fields = ['subject', 'lecturer', 'hall', 'start_time', 'end_time', 'days_of_week']

    days_of_week = forms.MultipleChoiceField(
        choices=[
            ('M', 'M'),
            ('T', 'T'),
            ('W', 'W'),
            ('Th', 'Th'),
            ('F', 'F'),
            ('Sa', 'Sa'),
            ('Su', 'Su'),
        ],
        widget=forms.CheckboxSelectMultiple,
        required=False
    )


    def save(self, commit=True):
        instance = super().save(commit=False)
        # Convert list of days to a comma-separated string
        instance.days_of_week = ','.join(self.cleaned_data['days_of_week'])
        if commit:
            instance.save()
        return instance
    

from django import forms
from .models import Timetable


class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['subject', 'lecturer', 'hall', 'start_time', 'end_time', 'days_of_week']

    def clean(self):
        cleaned_data = super().clean()
        start_time = cleaned_data.get("start_time")
        end_time = cleaned_data.get("end_time")
        lecturer = cleaned_data.get("lecturer")
        hall = cleaned_data.get("hall")

        # Add validation logic to ensure no overlapping time slots
        if start_time and end_time and lecturer and hall:
            # Check for overlapping time slots in the database
            overlapping_slots = Timetable.objects.filter(
                lecturer=lecturer,
                hall=hall,
                start_time__lt=end_time,
                end_time__gt=start_time
            )
            if overlapping_slots.exists():
                raise forms.ValidationError("This lecturer and hall are already booked for this time slot.")

        return cleaned_data
    
#user account creation
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    birthdate = forms.DateField(required=True, widget=forms.SelectDateWidget(years=range(1900, 2023)))
    discord_id = forms.CharField(max_length=100, required=False)
    zoom_id = forms.CharField(max_length=100, required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'birthdate', 'discord_id', 'zoom_id']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'birthdate': forms.Select(attrs={'class': 'form-control'}),
            'discord_id': forms.TextInput(attrs={'class': 'form-control'}),
            'zoom_id': forms.TextInput(attrs={'class': 'form-control'}),
        }