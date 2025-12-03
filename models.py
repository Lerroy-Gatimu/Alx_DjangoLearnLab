from django.db import models

# Create your models here.
# advanced_features_and_security/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .advanced_features_and_security.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None  # We don't use username
    email = models.EmailField(_("email address"), unique=True)

    date_of_birth = models.DateField(_("date of birth"), null=True, blank=True)
    profile_photo = models.ImageField(
        _("profile photo"),
        upload_to="profile_photos/",
        null=True,
        blank=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def __str__(self):
        return self.email