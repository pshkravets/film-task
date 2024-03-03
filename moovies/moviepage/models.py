from django.db import models

''' Actor table, relative To Moovie table through ManyToManyField(Actors)'''
class Actor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

''' Producer table, relative To Moovie table through Foreignkey(producer)'''
class Producer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
''' Main table '''
class Moovie(models.Model):
    name = models.CharField(max_length=30)
    release_year = models.IntegerField()
    actors = models.ManyToManyField(Actor)
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
