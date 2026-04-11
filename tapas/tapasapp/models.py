from django.db import models

# Create your models here.

class Dish(models.Model):
    name = models.CharField(max_length=300)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.name

class Account(models.Model):
    name = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()

    def __str__(self):
        return str(self.pk) + ": " + self.name
    def getUsername():
        return self.name
    def getPassword():
        return self.password
    