from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Contact = models.IntegerField(null=True,blank=True)
    Message = models.TextField(max_length=300, null=True, blank=True)

class RegisterDb(models.Model):
    Name = models.CharField(max_length=100, null=True, blank=True)
    Mobile = models.IntegerField(null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    CPassword = models.CharField(max_length=100, null=True, blank=True)

class CartDb(models.Model):
    Username = models.CharField(max_length=100,null=True,blank=True)
    ProductName = models.CharField(max_length=100,null=True,blank=True)
    Quantity = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
    Price = models.IntegerField(null=True,blank=True)
    Prod_Image = models.ImageField(upload_to="Cart_Images",null=True,blank=True)
class OrderDb(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email = models.CharField(max_length=100,null=True,blank=True)
    Place = models.CharField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100,null=True,blank=True)
    Mobile = models.IntegerField(null=True,blank=True)
    State = models.CharField(max_length=100,null=True,blank=True)
    Pin = models.IntegerField(null=True,blank=True)
    TotalPrice = models.IntegerField(null=True,blank=True)
    Messages = models.TextField(max_length=300,null=True,blank=True)