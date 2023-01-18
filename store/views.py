from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProductSerializer
from .models import Product

from .exceptions import ProductNotFound


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer



class ProductDetailView(APIView):

    def get(self, request, id):
        
        try:
            product = Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise ProductNotFound

        serializer = ProductSerializer(product, context = {'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)