# myapp/models.py
# models.py

from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
