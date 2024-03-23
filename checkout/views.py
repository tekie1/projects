from django.shortcuts import render, redirect

from cart.models import Cart
from checkout.models import Order, ShippingAddress, ShippingMethod, ShippingZone

from .forms import ShippingAddressForm
from django.shortcuts import get_object_or_404
from django.contrib import messages


def shipping_address_view(request):
    if request.method == "POST":
        form = ShippingAddressForm(request.POST)
        if form.is_valid():
           
            shipping_address = form.save(
                commit=False
            ) 
            shipping_address.user = (
                request.user
            ) 
            if not shipping_address:
                shipping_address.save()  
          
            return redirect(
                "choose_shipping_method"
            ) 
    else:
        form = ShippingAddressForm()
    return render(request, "shipping_address.html", {"form": form})


def choose_shipping_method(request):
    user = request.user
    shipping_address = get_object_or_404(ShippingAddress, user=user)
    country = shipping_address.country
    available_shipping_methods = get_available_shipping_methods(country)
    return render(
        request,
        "choose_shipping_method.html",
        {"shipping_methods": available_shipping_methods},
    )


def get_available_shipping_methods(customer_country):
    try:
        shipping_zone = ShippingZone.objects.get(countries__name=customer_country)
        available_methods = ShippingMethod.objects.filter(zones=shipping_zone)
        return available_methods
    except ShippingZone.DoesNotExist:
        return None


def update_order_total(order_id, new_total):
    
    order = Order.objects.get(id=order_id)
    order.total = new_total
    order.save()


def calculate_shipping_cost(selected_shipping_method):
   
    if selected_shipping_method == "Standard":
        return 5.0
    elif selected_shipping_method == "Express":
        return 10.0 
    else:
        return 0.0  


from django.shortcuts import render, redirect
from django.contrib import messages


def process_checkout(request):
    if request.method == "POST":
      
        selected_shipping_method = request.POST.get("shipping_method")

       
        shipping_cost = calculate_shipping_cost(selected_shipping_method)
        cart = Cart.objects.filter(user=request.user).first()
        if not cart:
            messages.info(request, "Your cart is empty.")
            return render(request, "cart.html", {"cart_items": []})

        cart_items = cart.items.all()
        total_cart_items = sum(item.quantity for item in cart_items)
        total_price = sum(item.total_price() for item in cart_items)
        tax = (float(total_price) / 100) * 5
        total_order_price = float(total_price) + float(tax) + float(shipping_cost)

        return render(
            request,
            "order_summary.html",
            {
                "total_items": total_cart_items,
                "total_order_price": total_order_price,
                "shipping_cost": shipping_cost,
                "tax": tax,
            },
        )
    else:
     
        pass
