# from django.contrib.auth.forms import UserCreationForm
# from .models import User
# from django.contrib.auth.forms import AuthenticationForm
from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(min_value=1)

    def clean_quantity(self):
        quantity = self.cleaned_data.get("quantity")
        if quantity < 1:
            raise forms.ValidationError("Quantity must be at least 1.")
        return quantity
