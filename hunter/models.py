from django.db import models

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=40)


    def __str__(self):

        return self.location_name


class House(models.Model):
    title = models.CharField(max_length=40)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    type = models.Choices()
    units = models.IntegerField()
    kitchen = models.IntegerField()
    parking = models.IntegerChoices()


    def __str__(self):

        return self.title