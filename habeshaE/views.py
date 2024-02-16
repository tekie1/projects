from django.shortcuts import render
# views.py

from .models import Category, UploadedImage


# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the habeshaE index.")
# accounts/views.py

# views.py
from django.shortcuts import redirect

from .forms import CustomUserCreationForm

from django.contrib.auth import login
from .forms import UserLoginForm

from django.db.models import Q


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)  
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()

    return render(request, "login/login.html", {"form": form})


# views.py


def home(request):
    if request.method == "POST":
        print("POST data:", request.POST)

        category = request.POST.get("category")
        keyword = request.POST.get("keyword")
        print("Selected category:", category)

        products = UploadedImage.objects.all()
        categories = Category.objects.all()

        if "search_performed" in request.POST:
            search_performed = True
            if category:
                products = products.filter(category=category)
            if keyword:
                # Filter products where the name contains the keyword or the description contains the keyword
                products = products.filter(
                    Q(name__icontains=keyword) | Q(description__icontains=keyword)
                )
    else:
        search_performed = False
        products = UploadedImage.objects.all()
        categories = Category.objects.all()

    return render(
        request,
        "home.html",
        {
            "products": products,
            "categories": categories,
            "search_performed": search_performed,
        },
    )


def upload_image(request):
    images = UploadedImage.objects.all()
    return render(request, "home.html", {"images": images})
