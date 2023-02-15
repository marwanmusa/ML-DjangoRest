from django.db import models
from django.db.models.manager import Manager


class FaceRecognition(models.Model):
    name = models.CharField(max_length=255)
    device = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=255)

    objects = Manager()

    class Meta:
        ordering = ['id']
