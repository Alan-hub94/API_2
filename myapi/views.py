from rest_framework import viewsets

from .serializers import ProductoSerializer
from .models import Producto

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('name')
    serializer_class = ProductoSerializer


