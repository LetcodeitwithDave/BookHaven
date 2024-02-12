from django.db import models
from django.contrib.auth.models import User, AbstractUser



# Create your models here.
class Profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE , null = True)
    username = models.CharField(max_length=50)
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
    name = models.CharField(max_length=200)
    price =  models.IntegerField()
    quantity =  models.IntegerField()
    image = models.ImageField(upload_to= 'images/')
    created = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return f"username - {self.name}, email = {self.price}, quantity = {self.quantity},  image = {self.image}, , created = {self.created}"




class Order(models.Model):
    ORDER_STATUS_CHOICE = [
        ('p', 'pending'),
        ('d','dilivered'),
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length= 230)
    number = models.IntegerField()
    email = models.EmailField()
    method = models.CharField(max_length= 100)
    address = models.CharField(max_length = 300)
    total_product = models.CharField(max_length = 10000)
    total_price = models.IntegerField()
    placed_on = models.DateTimeField(auto_now_add=True, null = True)
    payment_status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICE, default = 'p')
    
    def __str__(self):
        return f"[name - {self.name}, number = {self.number}, address = {self.address},  total_product = {self.total_product}, total_price = {self.total_price}, payment_status = {self.payment_status}]"


class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.IntegerField()
    message = models.CharField(max_length=1000)
    
    def __str__(self):
        return f"[name = {self.name}, email = {self.email}, number = {self.number},  message = {self.message}]"


