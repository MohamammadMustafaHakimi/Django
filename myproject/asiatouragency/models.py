from django.db import models

# Create your models here.
class Tour(models.Model):
    origin_country = models.CharField(max_length=64)
    destination_country = models.CharField(max_length=64)
    number_of_nights = models.IntegerField()
    price = models.IntegerField()

    # this is a string representation of the tours
    def __str__(self):
        return (f"ID:{self.id} : From {self.origin_country} To {self.destination_country},{self.number_of_nights} nights costs ${self.price}") # you don't have to worry about the id; django will add an id, each time you add a record
