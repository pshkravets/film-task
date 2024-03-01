from django.db import models


class Actor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Producer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Moovie(models.Model):
    name = models.CharField(max_length=30)
    release_year = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
