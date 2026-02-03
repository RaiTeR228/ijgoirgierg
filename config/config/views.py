from rest_framework import viewsets
from hors.models import Product
from hors.serializers import HorsProductSerializer

class HorsProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # Модель Product из приложения hors
    serializer_class = HorsProductSerializer