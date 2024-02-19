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
        if not obj.stock:
            obj.stock = 0  
        obj.save()  

    list_display = ("name", "category", "price")  
    list_filter = ("category",) 
    search_fields = (
        "name",
        "description",
    )  


admin.site.register(Category)
admin.site.register(User)
admin.site.register(UploadedImage, UploadedImageAdmin)
