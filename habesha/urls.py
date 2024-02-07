from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings

from django.conf.urls.static import static

from habeshaE import views
def redirect_to_login(request):
    return redirect('login')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_login, name='index'),  # Redirect empty path to login page
    path('home/', include('habeshaE.urls')),
    # path('register/', include('habeshaE.urls')),
    path('login/', include('habeshaE.urls')),
     path('upload/', views.upload_image, name='upload_image'),
    path('habesha/', include('habeshaE.urls')),
    # Add other URL patterns as needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)