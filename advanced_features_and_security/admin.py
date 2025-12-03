from django.contrib import admin

# Register your models here.
# advanced_features_and_security/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(BaseUserAdmin):
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser

    list_display = ("email", "first_name", "last_name", "date_of_birth", "is_staff", "is_active")
    list_filter = ("is_staff", "is_superuser", "is_active")
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "first_name", "last_name", "date_of_birth", "profile_photo", "is_staff", "is_active"),
        }),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions",)


admin.site.unregister(CustomUser)  # Just in case
admin.site.register(CustomUser, CustomUserAdmin)