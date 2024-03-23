from django.contrib import admin

from products.models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    """Admin"""

    def save_model(self, request, obj, form, change):
        if not obj.price:
            obj.price = 0.00
        if not obj.description:
            obj.description = ""
        if not obj.stock:
            obj.stock = 0
        obj.save()

    list_display = ("name", "category", "price")
    list_filter = ("category",)
    search_fields = (
        "name",
        "description",
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display=("name",)
admin.site.register(Category,CategoryAdmin)

admin.site.register(Product, ProductAdmin)
