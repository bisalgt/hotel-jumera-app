from django.db import models
from django.urls import reverse


class Gallery(models.Model):
    gallery_image_title = models.CharField(max_length=200)
    gallery_image = models.ImageField(upload_to='gallery_pics')

    def __str__(self):
        return self.gallery_image_title

    def get_absolute_url(self):
        return reverse('gallery_list')


class GalleryUploads(models.Model):
    upload_image_title = models.CharField(max_length=200)
    upload_image = models.ImageField(upload_to='gallery_upload_pics')

    def __str__(self):
        return self.upload_image_title

    def get_absolute_url(self):
        return reverse('gallery_upload_list')
