from django.db import models

class About(models.Model):
    image = models.ImageField(upload_to='about_pics')
    about = models.TextField()
