from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    
class Food(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField(null = True,blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField()
    
class Table(models.Model):
    number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=False)
    
class Order(models.Model):
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    foods = models.ForeignKey(Food, on_delete=models.PROTECT)