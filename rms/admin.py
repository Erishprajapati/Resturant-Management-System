from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Food)
class Food(admin.ModelAdmin):
    list_display = ['id','name','description','category','price']
    list_editable = ['name','price','category']
    search_fields = ['name','category']
    list_filter = ('name',)
    readonly_fields = ['id','name']
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1
    
@admin.action(description="Mark selected orders as completed")
def mark_as_completed(modeladmin, request, queryset):
    queryset.update(status="Completed")
    
@admin.register(Order)
class Order(admin.ModelAdmin):
    list_display = ['user_id','status','quantity', 'payment', 'total_price']
    list_editable = ['status']
    inlines = [OrderItemInline]
    actions = [mark_as_completed]
    
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ['name']
    # list_editable = ['name']
    
@admin.register(Table)
class Table(admin.ModelAdmin):
    list_display = ['number','is_available']
    list_editable = ['is_available']
