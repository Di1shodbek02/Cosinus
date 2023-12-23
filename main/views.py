from datetime import datetime

from django.db.models import Q
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Product
from .serializer import ProductSerializer


class AddProductAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def post(self, request):
        product_serializer = self.get_serializer(data=request.data)
        product_serializer.is_valid(raise_exception=True)
        product_serializer.save()
        return Response(product_serializer.data)


class ProductUpdateGenericAPIView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ProductSerializer

    def patch(self, request, pk):
        try:
            product = Product.objects.get(Q(pk=pk, user=request.user))
            serializer = self.get_serializer(product, request.data, partial=True)
            serializer.validated_data['update_time'] = datetime.utcnow()
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Exception as e:
            return Response({"status": False, "message": str(e)})

    def delete(self, request, pk):
        try:
            product = Product.objects.get(Q(pk=pk) & Q(user=request.user))
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({"status": False, "message": str(e)})


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = ()
