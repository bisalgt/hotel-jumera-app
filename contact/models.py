from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    message = models.TextField()

    def __Str__(self):
        return self.name