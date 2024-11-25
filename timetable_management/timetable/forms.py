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