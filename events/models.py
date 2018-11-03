from django.db import models
from django.utils import timezone
from PIL import Image

class PastEvent(models.Model):
    title = models.CharField(max_length=200, default='Title')
    image = models.ImageField(upload_to='event_pics')
    time = models.DateTimeField(default=timezone.now())
    description = models.TextField()

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height != 768 or img.width != 1366:
            output_size=(1366, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)


class FutureEvent(models.Model):
    title = models.CharField(max_length=200, default='Title')
    image = models.ImageField(upload_to='event_pics')
    time = models.DateTimeField(default=timezone.now())
    description = models.TextField()

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height != 768 or img.width != 1366:
            output_size=(1366, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)
