from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Food)
class Food(admin.ModelAdmin):
    list_display = ['id','name','description','category','price']
    list_editable = ['name','price','category']
    search_fields = ['name','category']
    list_filter = ('name',)
    
@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['user_id','status','quantity', 'payment', 'total_price']
    list_editable = ['status']
    
admin.site.register(OrderItem)
admin.site.register(Category)
admin.site.register(Table)
    

