from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='services_pics')
    title = models.CharField(max_length=50, default='None Heading/none')
    description = models.CharField(max_length=300)
