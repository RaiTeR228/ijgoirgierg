from rest_framework import serializers
from .models import Product

class CarProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # или можно указать конкретные поля: ['id', 'name', 'price', 'in_stock', 'create_at']