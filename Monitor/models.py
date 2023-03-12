from django.db import models


class Plant(models.Model):
    serial = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=256)

class User(models.Model):
    userId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    plant = models.ManyToManyField(Plant)