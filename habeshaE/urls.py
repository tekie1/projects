from django.urls import path
from habeshaE import views



urlpatterns = [
    path("", views.index, name="index"),
]