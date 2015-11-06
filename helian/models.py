import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20)
    givenname = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

class Department(models.Model):
    name = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Person)
    pass

class Status(models.Model):
    devicestatus = models.CharField(max_length=100)
    uptime = models.DateTimeField()
    pass

class PowerUsage(models.Model):
    unitsconsumed = models.FloatField()
    recordedon = models.DateTimeField()
    pass

class Device(models.Model):
    name = models.CharField(max_length=200)
    dept = models.ForeignKey(Department)
    status = models.ForeignKey(Status)
    usage = models.ForeignKey(PowerUsage)
    pass
