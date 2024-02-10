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
    created = models.DateTimeField(auto_now_add=True, null = True)
    def __str__(self):
        return f"name= {self.name}, price = {self.price}, image = {self.image}, created = {self.created}"


class Cart(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, unique= True)
    price =  models.IntegerField()
    quantity =  models.IntegerField()
    image = models.ImageField(upload_to= 'images/')
    created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return f"username - {self.name}, email = {self.price}, quantity = {self.quantity},  image = {self.image}, , created = {self.created}"


    def sum_total(self):
        return self.quantity * self.price
