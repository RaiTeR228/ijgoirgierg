from rest_framework import viewsets
from .models import Product
from .serializers import KmProductSerializer

class KmProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Здесь Product - это модель из приложения km
    serializer_class = KmProductSerializer