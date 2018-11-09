from django.db import models
from django import forms

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    message = models.CharField(max_length=250)

    def __str__(self):
        return self.name
