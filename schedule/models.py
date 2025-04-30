from django.db import models


class Schedule(models.Model):
    date_range = models.CharField(max_length=255)
    image = models.ImageField()
