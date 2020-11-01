
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import base64


class Contact(models.Model):
    email = models.CharField(max_length=128)
    phoneNo = models.CharField(max_length=128)

  #  def __str__(self):
    #    return self.email, self.phoneNo


class Orders(models.Model):
    order_id = models.BinaryField(max_length=15, unique=True, editable=False)
    quantity = models.CharField(max_length=32)


class Products(models.Model):
    products_id = models.BinaryField(
    max_length=15, unique=True, editable=False)
    quantity = models.CharField(max_length=32)
    price = models.CharField(max_length=32)

    #name = models.CharField(max_length=128, blank=True)
    #access_to_doors = models.ManyToManyField(Door, blank=True)

#    def __str__(self):
 #       return self.quantity, self.price


class Users(models.Model):

    uid = models.BinaryField(max_length=15, unique=True, editable=False)
    active = models.BooleanField(default=True)
    note = models.CharField(blank=True, max_length=128)
    username = models.CharField(max_length=128)
    #owner = models.ForeignKey(User, on_delete=models.PROTECT)
    #access_to_doors = models.ManyToManyField(Products)
    #groups_member = models.ManyToManyField(Group)

    def __str__(self):
        return base64.b64encode(self.uid).decode('ascii')
        return self.username


class Reviews(models.Model):
    reviews_id = models.BinaryField(max_length=15, unique=True, editable=False)
    reviews_name = models.CharField(max_length=32)
    username = models.ManyToManyField(Users)

  #  def __str__(self):
   #     return self.reviews_id
