from django.contrib.auth.forms import UserCreationForm

from apps.core.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name")
        labels = {"first_name": "Primeiro nome"}
