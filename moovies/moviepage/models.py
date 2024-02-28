from django.db import models


class Producer(models.Model):
    name = models.CharField(max_length=30)

class Actor(models.Model):
    name = models.CharField(max_length=30)

class Moovie(models.Model):
    name = models.CharField(max_length=30)
    release_year = models.DateField()
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    actor = models.ForeignKey(Actor, on_delete=models.PROTECT)
