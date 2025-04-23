from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    tag = models.ForeignKey(
        Tag, 
        on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE)
    body = models.TextField()
    

    def __str__(self):
        return self.title