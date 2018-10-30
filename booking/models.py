from django.db import models
from datetime import datetime, timedelta
from django.urls import reverse
from rooms.models import RoomDetail


class Booking(models.Model):
    room = models.ForeignKey(RoomDetail, on_delete=models.CASCADE)
    check_in = models.DateField(default=datetime.now())
    check_out = models.DateField(default=datetime.now()+timedelta(days=1))
    adult = models.PositiveIntegerField(default=3)
    child = models.PositiveIntegerField(default=0)

    def get_absolute_url(self):
        return reverse('booking_success_detail',args=[str(self.id)])
