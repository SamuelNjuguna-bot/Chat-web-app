from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    room = models.CharField(max_length=100000)
class Message(models.Model):
    message = models.CharField(max_length=1000000)
    username = models.CharField(max_length=100000)
    room =models.CharField(max_length=100000)
    date = models.DateTimeField(default=datetime.now, blank=True)