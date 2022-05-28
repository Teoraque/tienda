from xml.etree.ElementInclude import include
from rest_framework import routers
from django.urls import path, include

from . import views

router_producto = routers.DefaultRouter()
router_producto.register("productos", views.Productoview)

urlpatterns = [
    path("", include(router_producto.urls), name="producto")
]