from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Location(models.Model):
    location_name = models.CharField(max_length=40)


    def __str__(self):

        return self.location_name


HOUSE_CHOICES = [
    ('Apartment', 'Apartment.'),
    ('Condo', 'Condo.'),
    ('Bungalow', 'Bungalow.'),
]



class House(models.Model):
    title = models.CharField(max_length=40)
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField()
    house_type = models.CharField(max_length=20, choices=HOUSE_CHOICES)
    units = models.IntegerField()
    kitchen = models.IntegerField()
    parking = models.IntegerField()
    house_location = models.OneToOneField(Location,on_delete=models.DO_NOTHING)
    house_image = CloudinaryField("house_image")

    def __str__(self):

        return self.title

    class Meta:
        ordering = ['title']