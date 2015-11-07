import datetime

from django.db import models
from django.template.defaultfilters import default

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20,null=False,default='unspecified')
    givenname = models.CharField(max_length=30,null=True)
    surname = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=50, null=False, default='unspecified@sitebrain.com')
    
class Department(models.Model):
    name = models.CharField(max_length=20,default='unspecified')
    supervisor = models.ForeignKey(Person)

class Status(models.Model):
    name = models.CharField(max_length=20,default='unspecified')
    def __unicode__(self):
        return self.name
        
class Device(models.Model):
    
    name = models.CharField(max_length=20,default='unspecified')
    dept = models.ForeignKey(Department, null=True)
    owner = models.ForeignKey(Person, null=True)
    status = models.ForeignKey(Status, null=True)
    lastmodified = models.DateTimeField(default=datetime.datetime.now())
    
class PowerUsage(models.Model):
    unitsconsumed = models.FloatField()
    temperature = models.FloatField(default='0.0')
    device = models.ForeignKey(Device, null=True)
    lastrecorded = models.DateTimeField(default=datetime.datetime.now())