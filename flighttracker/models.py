from django.db import models

class Passenger(models.Model):
    id            = models.IntegerField(primary_key=True)
    first_name    = models.CharField(max_length=25, blank=False, null=False, default='')
    last_name     = models.CharField(max_length=25, blank=False, null=False, default='')
    flight_points = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.first_name + " " + self.last_name

