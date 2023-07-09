from rest_framework.response import Response
from rest_framework import viewsets
from .models import Category, Brand, Product
from .serializers import CategorySerializer, BrandSerializer, ProductSerializer
from drf_spectacular.utils import extend_schema


@extend_schema(responses=CategorySerializer)
class CategoryViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """
    queryset = Category.objects.all()

    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


@extend_schema(responses=BrandSerializer)
class BrandViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing categories
    """
    queryset = Brand.objects.all()

    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

@extend_schema(responses=ProductSerializer)
class ProductViewSet(viewsets.ViewSet):
    """
    A simple Viewset for viewing products
    """
    queryset = Product.objects.all()

    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)