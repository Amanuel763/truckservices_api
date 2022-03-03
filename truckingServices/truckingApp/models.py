from django.db import models

# Create your models here.
class Routes(models.Model):
    truckdriver = models.CharField(max_length=30)
    routeNumber = models.CharField(max_length=30)
    departureCity = models.CharField(max_length=30)
    arrivalCity = models.CharField(max_length=30)
    dateOfDeparture = models.DateField()
    estimatedTimeOfDeparture = models.TimeField()

class Driver(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    middleName = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=25)

