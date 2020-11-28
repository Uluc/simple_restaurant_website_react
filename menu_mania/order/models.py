from django.db import models
from restaurant.models import Restaurant
from customer.models import Customer
from menu.models import Dish

class Order(models.Model):
    restaurant = models.ForeignKey("restaurant.Restaurant", on_delete=models.CASCADE)
    customer = models.ForeignKey("customer.Customer", on_delete=models.CASCADE)
    time_ordered = models.DateTimeField(auto_now=True)
    time_delivered = models.DateTimeField()
    dish = models.ForeignKey("menu.Dish", on_delete=models.CASCADE)