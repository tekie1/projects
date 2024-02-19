from django.shortcuts import render
# views.py

from .models import Category, UploadedImage
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Cart, CartItem
from django.contrib.auth.decorators import login_required
from .forms import AddToCartForm

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
    total_cart_items = 0
    cart_content = False
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(cart__user=request.user)
        total_cart_items = sum(item.quantity for item in cart_items)
        if "cart_clicked" in request.GET:
            cart_content = True
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
            "total_cart_items": total_cart_items,
        },
    )


def upload_image(request):
    images = UploadedImage.objects.all()
    return render(request, "home.html", {"images": images})


# views.py


@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(UploadedImage, pk=product_id)
    form = AddToCartForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        quantity = form.cleaned_data["quantity"]
        if quantity > product.stock:
            messages.error(request, "Insufficient stock.")
            return redirect("product_detail", product_id=product_id)

        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
            messages.success(request, "Product quantity updated in the cart.")
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Product added to the cart.")

        return redirect("cart")

    return render(request, "add_to_cart.html", {"form": form, "product": product})


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)

    if cart_item.cart.user != request.user:
        messages.error(request, "You do not have permission to remove this item.")
        return redirect("cart")

    cart_item.delete()
    messages.success(request, "Product removed from the cart.")
    return redirect("cart")


@login_required
def edit_cart_item(request, item_id):
    cart_item = get_object_or_404(CartItem, pk=item_id)

    if cart_item.cart.user != request.user:
        messages.error(request, "You do not have permission to edit this item.")
        return redirect("cart")

    if request.method == "POST":
        quantity = int(request.POST.get("quantity", 0))
        if quantity <= 0:
            cart_item.delete()
            messages.success(request, "Product removed from the cart.")
        elif quantity > cart_item.product.stock:
            messages.error(request, "Insufficient stock.")
        else:
            cart_item.quantity = quantity
            cart_item.save()
            messages.success(request, "Cart item quantity updated.")
        return redirect("cart")

    return render(request, "edit_cart_item.html", {"cart_item": cart_item})


@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    if not cart:
        messages.info(request, "Your cart is empty.")
        return render(request, "cart.html", {"cart_items": []})

    cart_items = cart.items.all()
    total_price = sum(item.total_price() for item in cart_items)
    return render(
        request, "cart.html", {"cart_items": cart_items, "total_price": total_price}
    )


def product_detail(request, product_id):
    form = AddToCartForm(request.POST or None)
    product = get_object_or_404(UploadedImage, pk=product_id)
    return render(request, "product_detail.html", {"form": form, "product": product})
