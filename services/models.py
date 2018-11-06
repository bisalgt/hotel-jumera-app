from django.db import models
from PIL import Image
from django.utils import timezone


class Service(models.Model):
    image = models.ImageField(upload_to='services_pics')
    title = models.CharField(max_length=50, default='None Heading/none')
    description = models.CharField(max_length=300)
    date = models.DateField(default=timezone.now)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title


    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height !=768 or img.width !=1366:
            output_size = (1366,768)
            img.thumbnail(output_size)
            img.save(self.image.path)
