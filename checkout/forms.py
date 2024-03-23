from django import forms

from checkout.models import ShippingAddress


class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        exclude = [
            "user",
        ]

    # full_name = forms.CharField(label="Full Name", max_length=100)
    address_line_1 = forms.CharField(label="Address Line 1", max_length=255)
    address_line_2 = forms.CharField(
        label="Address Line 2", max_length=255, required=False
    )
    city = forms.CharField(label="City", max_length=100)
    state_province = forms.CharField(label="State/Province", max_length=100)
    postal_code = forms.CharField(label="Postal Code", max_length=20)
    country = forms.CharField(label="Country", max_length=100)
    # phone = forms.CharField(label="Phone Number", max_length=20)
    email = forms.EmailField(label="Email Address", max_length=100)
