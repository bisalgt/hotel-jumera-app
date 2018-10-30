from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='services_pics')
    description = models.CharField(max_length=300)
    
