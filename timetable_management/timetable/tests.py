from django.test import TestCase
from django.urls import reverse
from .models import Lecturer, Subject, Hall, TimeSlot


# Create your tests here.


class TimetableViewsTestCase(TestCase):
    def setUp(self):
        
        self.lecturer = Lecturer.objects.create(name="Lakshana Assalaarachchi")
        self.subject = Subject.objects.create(name="Management Information Systems")
        self.hall = Hall.objects.create(name="Mayo")
        self.timeslot = TimeSlot.objects.create(
            day_of_week="Tuesday", start_time="13:00", end_time="17:00"
        )

    def test_index_view(self):
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timetable/index.html')
        self.assertContains(response, "Tuesday")  

    def test_lecturers_list_view(self):
        
        response = self.client.get(reverse('lecturers_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timetable/lecturers.html')
        self.assertContains(response, "Lakshana Assalaarachchi")  

    def test_subjects_list_view(self):
       
        response = self.client.get(reverse('subjects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timetable/subjects.html')
        self.assertContains(response, "Management Information Systems")  

    def test_halls_list_view(self):
       



        response = self.client.get(reverse('halls_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'timetable/halls.html')
        self.assertContains(response, "Mayo") 