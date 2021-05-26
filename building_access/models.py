
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import base64


class Contact(models.Model):
    email = models.CharField(max_length=128)
    phoneNo = models.CharField(max_length=128)


class Order(models.Model):
    order_id = models.BinaryField(max_length=32, unique=True, editable=False)
    name = models.CharField(max_length=45)
    #note = models.CharField(blank=True, max_length=45)


class Product(models.Model):
    name = models.CharField(max_length=40)
    quantity = models.CharField(max_length=32)
    price = models.CharField(max_length=32)


    #name = models.CharField(max_length=128, blank=True)
    #access_to_doors = models.ManyToManyField(Door, blank=True)


class Review(models.Model):
    review_id = models.CharField(max_length=15)
    review_name = models.CharField(max_length=128)
    #username = models.ManyToManyField(Users)



