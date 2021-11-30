from django.contrib import admin
from .models import *

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'id', 'create_at', 'updated_at')
    list_filter = ('name', 'price')
    
admin.site.register(Products ,ProductsAdmin)