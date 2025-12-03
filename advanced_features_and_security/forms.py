# advanced_features_and_security/forms.py
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from ..models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ("email", "first_name", "last_name", "date_of_birth")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = "__all__"