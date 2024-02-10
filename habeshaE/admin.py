from django.contrib import admin




from .models import UploadedImage

class UploadedImageAdmin(admin.ModelAdmin):
    pass
    def save_model(self, request, obj, form, change):
        # Custom validation and handling of the price and description fields
        if not obj.price:
            obj.price = 0.00
        if not obj.description:
            obj.description = ''
        obj.save()

admin.site.register(UploadedImage, UploadedImageAdmin)



