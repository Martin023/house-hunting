from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=40)


    def __str__(self):

        return self.location_name


class House(models.Model):
    title = models.CharField(max_length=40)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_type = models.Choices()
    units = models.IntegerField()
    kitchen = models.IntegerField()
    parking = models.IntegerChoices()
    house_location = models.OneToOneField(Location)
    house_image = CloudinaryField("house_image")

    def __str__(self):

        return self.title