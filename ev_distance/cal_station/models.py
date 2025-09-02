from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class ChargingStation(models.Model):
    name = models.CharField(max_length=200)
    location = models.PointField()
    address = models.CharField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
