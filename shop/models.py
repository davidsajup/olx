from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Product(models.Model):
#     name=models.CharField(max_length=100)
    
class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='products')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price=models.FloatField()
    desc = models.TextField()
    img=models.ImageField(upload_to='products')
    location=models.CharField(max_length=255,null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)
    us = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.name
    
class Profile(models.Model):
    phone = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    us = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.us.username
