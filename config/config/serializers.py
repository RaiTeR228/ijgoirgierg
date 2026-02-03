from rest_framework import serializers
from hors.models import Product

class HorsProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

# BookSerializer удалён — создайте сериализатор при наличии модели Book.