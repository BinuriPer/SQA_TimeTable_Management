from django.db import models

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