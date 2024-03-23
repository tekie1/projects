from django.urls import path
from checkout import views


urlpatterns = [
    path("shipping_address/", views.shipping_address_view, name="shipping-address"),
    path(
        "choose_shipping_method/",
        views.choose_shipping_method,
        name="choose_shipping_method",
    ),
    path("order_summary/", views.process_checkout, name="order_summary"),
    
    # path("choose_shipping_method/", views.choose_shipping_method, name="choose_shipping_method"),
]
