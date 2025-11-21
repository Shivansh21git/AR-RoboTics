from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ("username", "email", "full_name", "phone", "is_staff", "is_active", "role")
    list_filter = ("is_staff", "is_active", "role")
    # fieldsets = ()
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("full_name", "email", "phone", "profile_image", "address")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
        ("Role", {"fields": ("role",)}),
    )
    
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "password1", "password2", "is_staff", "is_active"),
        }),
    )

    search_fields = ("username", "email", "phone")

    ordering = ("email",)