

from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import UploadedImage
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email', 'first_name', 'last_name', 'username')


class UserLoginForm(AuthenticationForm):
    # You can customize the form fields or keep them as is
    class Meta:
        model = User  # Use your User model
        fields = ['username', 'password']
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image',)