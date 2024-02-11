
from django.shortcuts import render
# views.py

from .models import UploadedImage



# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the habeshaE index.")
# accounts/views.py

# views.py
from django.shortcuts import  redirect

from .forms import CustomUserCreationForm

from django.contrib.auth import  login
from .forms import UserLoginForm


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)  # Corrected this line
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home') 
    else:
        form = UserLoginForm()

    return render(request, 'login/login.html', {'form': form})
def home(request):
   images = UploadedImage.objects.all()
   return render(request, 'home.html', {'images': images})


def upload_image(request):
     images = UploadedImage.objects.all()
     return render(request, 'home.html', {'images': images})