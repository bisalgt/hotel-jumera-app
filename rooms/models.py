from django.db import models
from django.urls import reverse
from PIL import Image


class RoomDetail(models.Model):
    room_image = models.ImageField(upload_to='rooms_pics')
    room_name = models.CharField(max_length=200)
    room_about = models.TextField()
    tv_choices = (('NONE','None'),('FLAT TV', 'Flat TV'),('FLAT LED TV', 'Flat Led TV'),)
    room_tv = models.CharField(max_length=20, choices=tv_choices, default='NONE')
    wifi_choices = (('NOT AVAILABLE', 'Not Available'),('AVAILABLE', 'Available'),)
    room_wifi = models.CharField(max_length=20, choices=wifi_choices, default='NOT AVAILABLE')
    ac_choices = (('NOT AVAILABLE', 'Not Available'),('AVAILABLE', 'Available'),)
    room_ac = models.CharField(max_length=30, choices=ac_choices, default='NOT AVAILABLE')
    bedroom_choices = ((1,'Single Bed'),(2,'Double Bed'),(3, 'Three Beds'),)
    room_bedroom = models.IntegerField(choices=bedroom_choices, default=1,)
    bathroom_choices = (('ATTACHED','Attached'),('NOT ATTACHED','Not Attached'),)
    room_bathroom = models.CharField(max_length=30, choices=bathroom_choices, default='ATTACHED')

    def __str__(self):
        return self.room_name

    def get_absolute_url(self):
        return reverse('room_list')

    def save(self):
        super().save()
        img = Image.open(self.room_image.path)
        if img.height!=768 or img.width!=1366:
            output_size = (1366,768)
            img.thumbnail(output_size)
            img.save(self.room_image.path)
