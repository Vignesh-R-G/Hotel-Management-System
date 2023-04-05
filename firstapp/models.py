from django.db import models

# Create your models here.
class Hotel(models.Model):
    img=models.ImageField(upload_to='pics')
class Orders1(models.Model):
    img1=models.ImageField(upload_to='orderpics')
    name=models.CharField(max_length=30)
    price=models.IntegerField()
class Reservation(models.Model):
    Name=models.CharField(max_length=30)
    MobileNumber=models.CharField(max_length=30)
    Email=models.CharField(max_length=30)
    Indate=models.CharField(max_length=30)
    Outdate=models.CharField(max_length=30)
class Reserve(models.Model):
    name=models.CharField(max_length=30)
    mno=models.CharField(max_length=30)
class Book(models.Model):
    name=models.CharField(max_length=30)
    mno=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    indate=models.CharField(max_length=30)
    outdate=models.CharField(max_length=30)
class Room(models.Model):
    name=models.CharField(max_length=30)
    mno=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    indate=models.CharField(max_length=30)
    outdate=models.CharField(max_length=30)
    room=models.CharField(max_length=30, null=True, blank=True)
class Comment(models.Model):
    name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    mno=models.CharField(max_length=30)
    comments=models.TextField()
class FoodOrder(models.Model):
    name=models.CharField(max_length=30)
    dname=models.CharField(max_length=30)
    price=models.CharField(max_length=30)
    date=models.CharField(max_length=30)

