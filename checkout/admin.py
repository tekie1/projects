from django.contrib import admin

from checkout.models import ShippingMethod, ShippingZone


from django.contrib import admin
from .models import Country, Region, ShippingMethod, ShippingZone


# Define an inline formset for ShippingZone
# class ShippingZoneInline(admin.TabularInline):
#     model = (
#         ShippingMethod.zones.through
#     )  # Use the through model for the many-to-many relationship
#     extra = 1


# # Register ShippingMethod admin
# @admin.register(ShippingMethod)
# class ShippingMethodAdmin(admin.ModelAdmin):
#     inlines = [ShippingZoneInline]


class CountryAdmin(admin.ModelAdmin):
    list_display = ["name", "code"]


class RegionAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "country_name"]

    def country_name(self, obj):
        return obj.country.name

    country_name.short_description = "Country"


class ShippingZoneAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_countries",
        "get_regions",
    )  # Customize displayed fields in the admin list
    filter_horizontal = (
        "countries",
        "regions",
    )  # Add filter_horizontal for ease of selection

    def get_countries(self, obj):
        return ", ".join([country.name for country in obj.countries.all()])

    def get_regions(self, obj):
        return ", ".join([region.name for region in obj.regions.all()])

    get_countries.short_description = "Countries"  # Set the column header for countries
    get_regions.short_description = "Regions"  # Set the column header for regions


from django.contrib import admin
from .models import ShippingMethod


class ShippingMethodAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "description",
        "estimated_delivery_time",
        "cost",
        "zones_list",
    )  # Customize displayed fields in the admin list

    def zones_list(self, obj):
        return ", ".join([zone.name for zone in obj.zones.all()])

    zones_list.short_description = "Zones"  # Set the column header for zones


# Register other models if needed
admin.site.register(ShippingZone, ShippingZoneAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(ShippingMethod, ShippingMethodAdmin)


# class ShippingMethodZoneInline(admin.TabularInline):
#     model = ShippingMethod.zones.through
#     extra = 1


# @admin.register(ShippingMethod)
# class ShippingMethodAdmin(admin.ModelAdmin):
#     inlines = [ShippingMethodZoneInline]


# @admin.register(ShippingZone)
# class ShippingZoneAdmin(admin.ModelAdmin):
