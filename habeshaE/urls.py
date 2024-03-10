from django.urls import path
# from .views import add_to_cart, logout_view, user_login, home, register
from habeshaE import views
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path("home/", views.home, name="home"),
    # path("register/", register, name="register"),
    # path("login/", user_login, name="login"),
    # path("upload/", views.upload_image, name="upload_image"),
    # path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    # path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    # path("cart/", views.view_cart, name="cart"),
    # path(
    #     "remove_from_cart/<int:item_id>/",
    #     views.remove_from_cart,
    #     name="remove_from_cart",
    # ),
    # path("edit_cart_item/<int:item_id>/", views.edit_cart_item, name="edit_cart_item"),
    path("logout/", views.logout_view, name="logout"),
]
