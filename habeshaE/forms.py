# from django.contrib.auth.forms import UserCreationForm
# from .models import User
# from django.contrib.auth.forms import AuthenticationForm
# from django import forms
# from .models import UploadedImage


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = UserCreationForm.Meta.fields + (
#             "email",
#             "first_name",
#             "last_name",
#             "username",
#         )


# class UserLoginForm(AuthenticationForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]


# class UploadImageForm(forms.ModelForm):
#     class Meta:
#         model = UploadedImage
#         fields = ("image",)
        # forms.py


# class AddToCartForm(forms.Form):
#     quantity = forms.IntegerField(min_value=1)
#     def clean_quantity(self):
#         quantity = self.cleaned_data.get("quantity")
#         if quantity < 1:
#             raise forms.ValidationError("Quantity must be at least 1.")
#         return quantity
