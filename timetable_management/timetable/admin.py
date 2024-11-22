from django.contrib import admin
from .models import Lecturer, Subject, Hall, TimeSlot
from .forms import TimeSlotForm

# Register your models here
admin.site.register(Lecturer)
admin.site.register(Subject)
admin.site.register(Hall)

class TimeSlotAdmin(admin.ModelAdmin):
    form = TimeSlotForm
    list_display = ('subject', 'lecturer', 'hall', 'start_time', 'end_time', 'get_days_of_week')

    def get_days_of_week(self, obj):
        return ", ".join(obj.days_of_week.split(','))  # Adjust based on how you store days_of_week
    get_days_of_week.short_description = 'Days of the Week'

# Register TimeSlot with the custom admin class
admin.site.register(TimeSlot, TimeSlotAdmin)