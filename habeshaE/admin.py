from django.contrib import admin


from .models import UploadedImage, Category, User


admin.site.site_header = "habeshaE administration "


class UploadedImageAdmin(admin.ModelAdmin):
    """Admin"""

    def save_model(self, request, obj, form, change):
        if not obj.price:
            obj.price = 0.00
        if not obj.description:
            obj.description = ""
            obj.save()

    list_display = ("name", "category", "price")  # Display category in the list view
    list_filter = ("category",)  # Add a filter for category
    search_fields = (
        "name",
        "description",
    )  # Add search functionality for name and description


admin.site.register(Category )
admin.site.register(User)
admin.site.register(UploadedImage, UploadedImageAdmin)
