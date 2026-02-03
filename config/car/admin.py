# hors/admin.py
from django.contrib import admin
from .models import Product

# Регистрируем модель для админки
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'in_stock', 'create_at']
    list_filter = ['in_stock', 'create_at']
    search_fields = ['name']