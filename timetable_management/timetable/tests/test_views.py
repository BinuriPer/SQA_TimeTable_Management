# timetable/tests/test_views.py

from django.test import TestCase
from django.urls import reverse
from timetable.models import Lecturer, Subject, Hall, TimeSlot

class LecturerViewTest(TestCase):

    def setUp(self):
        self.lecturer = Lecturer.objects.create(name='John Doe', position='Lecturer', hours_per_week=20)

    def test_lecturer_list_view(self):
        response = self.client.get(reverse('lecturer_list'))  # Replace 'lecturer_list' with your actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.lecturer.name)
        self.assertTemplateUsed(response, 'timetable/lecturer_list.html')  # Adjust template path as needed

class SubjectViewTest(TestCase):

    def setUp(self):
        self.lecturer = Lecturer.objects.create(name='John Doe', position='Lecturer', hours_per_week=20)
        self.subject = Subject.objects.create(name='Mathematics', weekly_hours=4, lecturer=self.lecturer)

    def test_subject_list_view(self):
        response = self.client.get(reverse('subject_list'))  # Replace 'subject_list' with your actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.subject.name)
        self.assertTemplateUsed(response, 'timetable/subject_list.html')  # Adjust template path as needed

class TimeSlotViewTest(TestCase):

    def setUp(self):
        self.lecturer = Lecturer.objects.create(name='John Doe', position='Lecturer', hours_per_week=20)
        self.subject = Subject.objects.create(name='Mathematics', weekly_hours=4, lecturer=self.lecturer)
        self.hall = Hall.objects.create(name='Room 101', capacity=30)
        self.timeslot = TimeSlot.objects.create(
            subject=self.subject,
            lecturer=self.lecturer,
            hall=self.hall,
            start_time='09:00',
            end_time='10:00',
            days_of_week='M,T'  # Example of days of the week
        )

    def test_timeslot_list_view(self):
        response = self.client.get(reverse('timeslot_list'))  # Replace 'timeslot_list' with your actual URL name
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.timeslot.subject.name)
        self.assertTemplateUsed(response, 'timetable/timeslot_list.html')  # Adjust template path as needed

    def test_create_timeslot_view(self):
        response = self.client.post(reverse('create_timeslot'), {
            'subject': self.subject.id,
            'lecturer': self.lecturer.id,
            'hall': self.hall.id,
            'start_time': '10:00',
            'end_time': '11:00',
            'days_of_week': ['M', 'W']  # Example of days of the week
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful creation
        self.assertTrue(TimeSlot.objects.filter(subject=self.subject, start_time='10:00').exists())
