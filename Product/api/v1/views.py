from rest_framework.viewsets import ModelViewSet
# from rest_framework import status
# from rest_framework.response import Response
from Product.models import Product
from .serializers import ProductSerializer
from rest_framework.filters import SearchFilter


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (SearchFilter,)
    search_fields=('seller__username','name')
