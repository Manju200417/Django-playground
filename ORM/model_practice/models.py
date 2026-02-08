from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    password = models.CharField()

    def __str__(self):
        return self.name


class Prodect(models.Model):
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)

    def __str__(self):
        return self.name
