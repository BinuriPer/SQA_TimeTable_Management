from django.db import models
from django.contrib.auth.models import AbstractUser 

class Lecturer(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)  # Example: "Assistant Lecturer"
    hours_per_week = models.IntegerField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    weekly_hours = models.IntegerField()
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Hall(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
    
class TimeSlot(models.Model):
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE)
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()

    # Use a TextField to store multiple days as a comma-separated string
    days_of_week = models.TextField(help_text="Comma-separated list of days of the week the time slot is available", default='M')

    def __str__(self):
        return f"{self.subject.name} - {self.start_time} to {self.end_time} on {self.days_of_week}"

from django.contrib.auth.models import AbstractUser 
from django.db import models

class CustomUser (AbstractUser ):
    is_admin = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('can_view_dashboard', 'Can view dashboard'),
            ('can_edit_profile', 'Can edit profile'),
            # Add any additional custom permissions here
        ]
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'
        # Specify related names to avoid clashes
        unique_together = ('username', 'email')  # Optional: if you want to enforce unique usernames and emails

    # Override the groups and user_permissions fields to add related_name
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Change this to avoid conflict
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Change this to avoid conflict
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Timetable(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    days_of_week = models.CharField(max_length=20)

class LeaveRequest(models.Model):
    lecturer = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    substitute = models.ForeignKey(CustomUser , on_delete=models.CASCADE, related_name='substitutes', null=True)
