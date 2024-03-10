from django.urls import path
from cart.views import add_to_cart,view_cart,remove_from_cart,edit_cart_item

urlpatterns = [
    
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="cart"),
    path(
        "remove_from_cart/<int:item_id>/",
        remove_from_cart,
        name="remove_from_cart",
    ),
    path("edit_cart_item/<int:item_id>/", edit_cart_item, name="edit_cart_item"),
      
   
]
