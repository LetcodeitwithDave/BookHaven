from django.contrib import admin 
from .models import Profile, Cart, Product, Order

class CartAdmin(admin.ModelAdmin):
    list_display = ["profile", "name", "price", "quantity", "image"]

class ProductAdmin(admin.ModelAdmin):
    list_display = ["profile", "name", "price", "quantity", "image"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["profile", "name", "number", "email", "method", "address", "total_product", "total_price", "placed_on","payment_status"]


# Register your models here.
admin.site.register(Profile)
admin.site.register(Cart, CartAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)