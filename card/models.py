from django.db import models

class Card(models.Model):

    img = models.ImageField(upload_to='card/')
    information = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True, null=True)