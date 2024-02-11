from django.urls import path
from .views import  user_login, home, register
from habeshaE import views

urlpatterns = [
    path('home/', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
   path('upload/', views.upload_image, name='upload_image'),
    
]
