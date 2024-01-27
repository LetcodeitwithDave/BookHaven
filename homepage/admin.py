from django.contrib import admin
from .models import Profile, Cart, Product

class CartAdmin(admin.ModelAdmin):
    list_display = ["profile", "name", "price", "quantity", "image"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["profile", "name", "price", "quantity", "image"]

# Register your models here.
admin.site.register(Profile)
admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)