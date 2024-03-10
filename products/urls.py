from django.urls import path

from products.views import upload_product,product_detail


urlpatterns = [
   
    path("upload/", upload_product, name="Product"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
   
  
]
