from django.test import TestCase
from django.urls import reverse
from timetable.models import Lecturer, Subject, Hall, TimeSlot

class ViewTests(TestCase):
    def setUp(self):
        # Create test data
        self.lecturer = Lecturer.objects.create(name="Ms. Upeksha Samarasighe", position="Temporary Assistant Lecturer", hours_per_week=20)
        self.hall = Hall.objects.create(name="Mayo", capacity=70)
        self.subject = Subject.objects.create(name="SQA", weekly_hours=9, lecturer=self.lecturer)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timetable/index.html')

    def test_lecturers_list_view(self):
        response = self.client.get(reverse('lecturers_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ms. Upeksha Samarasighe")

    def test_subjects_list_view(self):
        response = self.client.get(reverse('subjects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "SQA")

    def test_halls_list_view(self):
        response = self.client.get(reverse('halls_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mayo")
