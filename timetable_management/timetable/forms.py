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