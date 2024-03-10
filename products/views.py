from django.shortcuts import get_object_or_404, render
from cart.forms import AddToCartForm


from products.models import Product


def upload_product(request):
    images = Product.objects.all()
    return render(request, "home.html", {"images": images})


def product_detail(request, product_id):
    form = AddToCartForm(request.POST or None)
    product = get_object_or_404(Product, pk=product_id)
    return render(request, "product_detail.html", {"form": form, "product": product})
