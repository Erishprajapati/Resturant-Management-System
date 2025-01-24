from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    def __str__(self):
        return self.name 
    
class Food(models.Model):
    name = models.CharField( max_length=50)
    description = models.TextField(null = True,blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.IntegerField()
    
    def __str__(self):
        return f""" Name: {self.name},
        Price: {self.price},
        Description: {self.description}
        """
    
class Table(models.Model):
    number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=False)
    
    def __str__(self):
        return self.number
    
class Order(models.Model):
    PENDING = 'P'
    COMPLETED = 'C'
    STATUS_CHOICE = {
        PENDING : "Pending",
        COMPLETED : "Completed",
    }
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    table_id = models.ForeignKey(Table, on_delete=models.CASCADE)
    total_price = models.FloatField(null = True,blank = True)
    status = models.CharField(max_length=10, choices = STATUS_CHOICE,default = 'P')
    payment = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f""" Order by {self.user_id},
        Quanity={self.quantity},
        Total Payment={self.payment},
        Status={self.status}"""
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    foods = models.ForeignKey(Food, on_delete=models.PROTECT)
    