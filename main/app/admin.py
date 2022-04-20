from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserData, Category, Post, Comment, User

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description")


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "slug", "content", "author")


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "website", "content", "post")


class UserDataAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "created", "modified")


UserAdmin.list_display = ['username', 'email', 'first_name',
                          'last_name', 'is_superuser', 'is_staff', 'is_active', 'last_login']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(UserData, UserDataAdmin)
