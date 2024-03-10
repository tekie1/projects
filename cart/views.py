from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from products.models import Product

# from telnetlib import LOGOUT
# from django.http import JsonResponse
# from django.shortcuts import render
# # views.py


                  

from cart.models import Cart, CartItem

from cart.forms import AddToCartForm







@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
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
