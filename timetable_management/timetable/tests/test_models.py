from django.test import TestCase
from timetable.models import Lecturer, Subject, Hall, TimeSlot
from datetime import time

class ModelTests(TestCase):
    def setUp(self):
        # Create test data
        self.lecturer = Lecturer.objects.create(name="Ms. Upeksha Samarasighe", position="Temporary Assistant Lecturer", hours_per_week=20)
        self.hall = Hall.objects.create(name="Mayo", capacity=70)
        self.subject = Subject.objects.create(name="SQA", weekly_hours=3, lecturer=self.lecturer)

    def test_lecturer_creation(self):
        # Test lecturer string representation
        self.assertEqual(str(self.lecturer), "Ms. Upeksha Samarasighe")
        self.assertEqual(self.lecturer.hours_per_week, 20)

    def test_hall_creation(self):
        # Test hall string representation
        self.assertEqual(str(self.hall), "Mayo")
        self.assertEqual(self.hall.capacity, 50)

    def test_subject_creation(self):
        # Test subject association with lecturer
        self.assertEqual(self.subject.lecturer.name, "Ms. Upeksha Samarasighe")
        self.assertEqual(self.subject.weekly_hours, 5)

    def test_time_slot_creation(self):
        # Create a TimeSlot instance
        time_slot = TimeSlot.objects.create(
            subject=self.subject,
            lecturer=self.lecturer,
            hall=self.hall,
            start_time=time(9, 0),
            end_time=time(10, 0),
            days_of_week="M,T,W"
        )
        # Test string representation and field values
        self.assertEqual(str(time_slot), "SQA - 17:00:00 to 20:00:00 on M,T,W")
        self.assertEqual(time_slot.days_of_week, "M,T,W")
