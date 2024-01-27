from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE , null = True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"username = {self.username}, email = {self.email}"


class Product(models.Model):
    name = models.CharField(max_length=200)
    price =  models.IntegerField()
    quantity =  models.IntegerField(null = True)
    image = models.ImageField(upload_to= 'images/')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank = True)
    
    def __str__(self):
        return f"name= {self.name}, price = {self.price}, image = {self.image}"


class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    price =  models.IntegerField()
    quantity =  models.IntegerField()
    image = models.ImageField(upload_to= 'images/')

    def __str__(self):
        return f"username - {self.name}, email = {self.price}, quantity = {self.quantity},  image = {self.image}"



