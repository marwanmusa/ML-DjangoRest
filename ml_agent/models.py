from django.db import models
from django.db.models.manager import Manager

class WeightPrediction(models.Model):
    sex_male = 'Male'
    sex_female = 'Female'
    group_gender = [
        (sex_male, sex_male),
        (sex_female, sex_female)
    ]

    gender = models.CharField(max_length=255, choices=group_gender)
    height = models.PositiveSmallIntegerField()
    owner = models.ForeignKey('auth.user', related_name='data', on_delete=models.CASCADE)

    objects = Manager()

    class Meta:
        ordering = ['id']