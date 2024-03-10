from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings

from django.conf.urls.static import static
from authentication.views import register

from products.views import upload_product, product_detail
from cart.views import add_to_cart, view_cart, edit_cart_item, remove_from_cart


def redirect_to_login(request):
    """redirecting to login"""
    return redirect("login")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_login, name="index"),  # Redirect empty path to login page
    path("home/", include("habeshaE.urls")),
    path("login/", include("authentication.urls")),
    path("register/", register, name="register"),
    path("upload/", upload_product, name="upload_product"),
    path("product/<int:product_id>/", product_detail, name="product_detail"),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="cart"),
    path("edit_cart_item/<int:item_id>/", edit_cart_item, name="edit_cart_item"),
    path(
        "remove_from_cart/<int:item_id>/",
        remove_from_cart,
        name="remove_from_cart",
    ),
    # path("logout/", views.logout_view, name="logout"),
    path("habesha/", include("habeshaE.urls")),
    # Add other URL patterns as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
