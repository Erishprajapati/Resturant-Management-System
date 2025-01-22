from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=15)
    
    
    
class Food(models.Model):
    name = models.models.CharField( max_length=50)
    description = models.models.TextField(null = True,blank = True)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    price = models.
    
    
