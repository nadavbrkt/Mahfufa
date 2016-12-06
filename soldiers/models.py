from django.db import models

# Create your models here.

class Soldier(models.Model):
        _name = models.CharField(max_length=200)
        _id = models.CharField(max_length=7)