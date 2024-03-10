from django.urls import path
from .views import user_login, register
# from habeshaE import views
# from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register/", register, name="register"),
    path("login/", user_login, name="login"),
]
