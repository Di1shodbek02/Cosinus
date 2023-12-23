from django.urls import path

from main.views import AddProductAPIView, ProductUpdateGenericAPIView, ProductListAPIView

urlpatterns = [
    path('add-product', AddProductAPIView.as_view(), name='add_product'),
    path('update-product/<int:pk>', ProductUpdateGenericAPIView.as_view(), name='update_product'),
    path('product-list', ProductListAPIView.as_view(), name='product_list'),
]
