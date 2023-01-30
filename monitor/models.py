from django.db import models

class Prediction(models.Model):
    age = models.IntegerField
    gender = request.GET.get('gender')
    bp = request.GET.get('bp')
    cholesterol = request.GET.get('cholesterol')
    salt = request.GET.get('salt')
