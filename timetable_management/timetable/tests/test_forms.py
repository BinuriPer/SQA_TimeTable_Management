# timetable/tests/test_forms.py

class RegisterFormTest(TestCase):
    def test_register_form_valid(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpass',
            'password2': 'testpass',
            'birthdate': '1990-01-01',
            'discord_id': 'testdiscord',
            'zoom_id': 'testzoom'
        }
        form = RegisterForm(data=form_data)
        if not form.is_valid():
            print(form.errors)  # Print errors for debugging
        self.assertTrue(form.is_valid())

class TimeSlotFormTest(TestCase):
    def test_timeslot_form_invalid(self):
        form_data = {
            'subject': self.subject.id,
            'lecturer': self.lecturer.id,
            'hall': self.hall.id,
            'start_time': '10:00',
            'end_time': '09:00',  # Invalid time range
            'days_of_week': ['M', 'T']
        }
        form = TimeSlotForm(data=form_data)
        if form.is_valid():
            print(form.errors)  # Print errors for debugging
        self.assertFalse(form.is_valid())