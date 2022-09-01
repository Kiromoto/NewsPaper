from django.contrib import admin
from .models import Author, Category, Post, PostCategory, Comment


class PostAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Post._meta.get_fields()]
    list_display = ('author', 'post_title', 'post_rating', 'post_create_datetime')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('author_user', 'author_rating')


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
