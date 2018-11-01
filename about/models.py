from django.db import models
from PIL import Image


class About(models.Model):
    image = models.ImageField(upload_to='about_pics')
    about = models.TextField()

    def __str__(self):
        return self.about[:15]

    def save(self):
        super().save()
        img= Image.open(self.image.path)
        if img.height != 768 or img.width != 1366:
            output_size=(1366, 768)
            img.thumbnail(output_size)
            img.save(self.image.path)
