from django.db import models
from datetime import datetime, timedelta
from django.utils import timezone
from django.urls import reverse
from rooms.models import RoomDetail



class Booking(models.Model):
    name = models.CharField(max_length=100, default='Name Here')
    room = models.ForeignKey(RoomDetail, on_delete=models.CASCADE)
    check_in = models.DateField(default=timezone.now())
    check_out = models.DateField(default=timezone.now()+timedelta(days=1))
    adult = models.PositiveIntegerField(default=2)
    child = models.PositiveIntegerField(default=0)

    def __str__(self):
        return (self.name, self.room)

    def get_absolute_url(self):
        return reverse('booking_success_detail',args=[str(self.id)])
