from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.IntegerField()
    birthday = models.DateField()
