from django.db import models
from django.urls import reverse
from PIL import Image


class Gallery(models.Model):
    gallery_image_title = models.CharField(max_length=200)
    gallery_image = models.ImageField(upload_to='gallery_pics')
    gallery_image_description = models.TextField(default="About the description of the image")
    def __str__(self):
        return self.gallery_image_title

    def get_absolute_url(self):
        return reverse('gallery_list')

    def save(self):
        super().save()
        img = Image.open(self.gallery_image.path)
        if img.height!=768 or img.width!=1366:
            output_size = (1366,768)
            img.thumbnail(output_size)
            img.save(self.gallery_image.path)


class GalleryUploads(models.Model):
    upload_image_title = models.CharField(max_length=200)
    upload_image = models.ImageField(upload_to='gallery_upload_pics')

    def __str__(self):
        return self.upload_image_title

    def get_absolute_url(self):
        return reverse('gallery_upload_list')

    def save(self):
        super().save()
        img = Image.open(self.upload_image.path)
        if img.height!=768 or img.width!=1366:
            output_size = (1366,768)
            img.thumbnail(output_size)
            img.save(self.upload_image.path)
