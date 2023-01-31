from django.db import models
from django.db.models.manager import Manager

class Prediction(models.Model):
    sex_male = 'M'
    sex_females = 'F'
    group_sex = [
        (sex_male, sex_male),
        (sex_females, sex_females)
    ]

    bp_high = 'HIGH'
    bp_normal = 'NORMAL'
    bp_low = 'LOW'
    group_bp = [
        (bp_high, bp_high),
        (bp_normal, bp_normal),
        (bp_low, bp_low)
    ]

    chol_high = 'HIGH'
    chol_normal = 'NORMAL'
    chol_low = 'LOW'
    group_chol = [
        (chol_high, chol_high),
        (chol_normal, chol_normal),
        (chol_low, chol_low)
    ]

    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=255, choices=group_sex, default=sex_male)
    bp = models.CharField(max_length=255, choices=group_bp, default=bp_normal)
    cholesterol = models.CharField(max_length=255, choices=group_chol, default=chol_low)
    salt = models.FloatField()

    objects = Manager()

    class Meta:
        ordering = ['id']