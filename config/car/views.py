from rest_framework import viewsets
from .models import Product
from .serializers import CarProductSerializer

class CarProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Здесь Product - это модель из приложения car
    serializer_class = CarProductSerializer