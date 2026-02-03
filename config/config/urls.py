from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HorsProductViewSet
from car.views import CarProductViewSet

router = DefaultRouter()
router.register(r'hors-products', HorsProductViewSet)
router.register(r'car-products', CarProductViewSet, basename='car-products')


urlpatterns = [
    path('', include(router.urls)),

]