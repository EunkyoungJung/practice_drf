from django.db import models

class Customer(models.Model):
    firstName    = models.CharField(max_length=20)
    lastName     = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + " " + self.lastName

class Order(models.Model):
    product = models.CharField(max_length=20)
    quantity = models.SmallIntegerField()
    customer = models.ForeignKey(Customer, related_name="customers", on_delete=models.CASCADE)

