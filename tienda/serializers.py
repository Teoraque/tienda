from rest_framework import serializers

from .models import Producto

class Producterializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"