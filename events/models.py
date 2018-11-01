from django.db import models
from django.utils import timezone
from PIL import Image

class Event(models.Model):
    title = models.CharField(max_length=200, default='Title')
    image = models.ImageField(upload_to='event_pics')
    time = models.DateTimeField(default=timezone.now())
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height != 768 or img.width != 1366:
            output_size=(1366, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)
