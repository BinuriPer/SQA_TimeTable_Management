from django.test import TestCase
from timetable.forms import TimeSlotForm
from timetable.models import Lecturer, Subject, Hall
from datetime import time

class FormTests(TestCase):
    def setUp(self):
        # Create test data
        self.lecturer = Lecturer.objects.create(name="Ms. Upeksha Samarasighe", position="Temporary Assistant Lecturer", hours_per_week=20)
        self.hall = Hall.objects.create(name="Mayo", capacity=70)
        self.subject = Subject.objects.create(name="SQA", weekly_hours=9, lecturer=self.lecturer)

    def test_valid_form(self):
        # Test valid form data
        form_data = {
            'subject': self.subject.id,
            'lecturer': self.lecturer.id,
            'hall': self.hall.id,
            'start_time': time(9, 0),
            'end_time': time(10, 0),
            'days_of_week': ['M', 'T']
        }
        form = TimeSlotForm(data=form_data)
        self.assertTrue(form.is_valid())
        instance = form.save(commit=False)
        self.assertEqual(instance.days_of_week, "M,T")

    def test_invalid_form(self):
        # Test invalid form data (missing required fields)
        form_data = {
            'lecturer': self.lecturer.id,
            'hall': self.hall.id,
        }
        form = TimeSlotForm(data=form_data)
        self.assertFalse(form.is_valid())
