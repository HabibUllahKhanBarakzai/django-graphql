from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(null=False, blank=False)
    age = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    profession = models.CharField(max_length=250, blank=True, null=True)


class Car(models.Model):
    make = models.CharField(max_length=150, null=False, blank=False)
    model = models.CharField(max_length=150, null=False, blank=False)
    body_type = models.CharField(max_length=150, null=False, blank=False)
    owner = models.ForeignKey(Customer, on_delete=models.SET_NULL,
                              null=True, related_name="car")
