from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser, Tag, Post


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "is_manager",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "is_manager",
        )


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "is_manager",
    ]
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("is_manager",)}),)
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("is_manager",)}),)


class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "tag",
    ]

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CustomUser, CustomUserAdmin)