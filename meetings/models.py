from django.db import models


class Household(models.Model):
    household_id = models.CharField(max_length=255, unique=True)
    square_feet = models.FloatField()


class Attend(models.Model):
    household_id = models.CharField(max_length=255, unique=True)
    is_attend = models.BooleanField()
