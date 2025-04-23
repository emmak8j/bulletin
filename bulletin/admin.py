from django.contrib import admin
from .models import Post, Tag

class TagAdmin(admin.ModelAdmin):
    list_display = [
        "name",
    ]

class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "tag"
    ]

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)