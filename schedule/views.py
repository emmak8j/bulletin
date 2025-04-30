from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Schedule


class ScheduleListView(LoginRequiredMixin, ListView):
    model = Schedule
    template_name = "schedule.html" 