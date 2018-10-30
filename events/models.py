from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200, default='Title')
    image = models.ImageField(upload_to='event_pics')
    time = models.DateTimeField(default=timezone.now())
    description = models.TextField()
