from django.db import models

class Course(models.Model):
    id          = models.IntegerField(primary_key=True)
    name        = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    rating      = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.id + "" + self.name
