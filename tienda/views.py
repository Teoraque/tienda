from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Producto
from .serializers import Producterializer

# Create your views here.
class Productoview(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset  = Producto.objects.all()
    serializer_class = Producterializer