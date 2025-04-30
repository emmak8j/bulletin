from django.contrib import admin
from .models import Schedule

class ScheduleAdmin(admin.ModelAdmin):
    list_display = [
        "date_range",
    ]

admin.site.register(Schedule, ScheduleAdmin)