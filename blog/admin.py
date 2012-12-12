from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from blog.models import Post, Category
from blog.models import UserProfile


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'created', 'get_categories', 'is_published')
    list_filter = ['created', 'categories']
    search_fields = ['title']
    date_hierarchy = 'created'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'


class UserAdmin(UserAdmin):
    inlines = [UserProfileInline, ]

try:
    admin.site.unregister(User)
finally:
    admin.site.register(User, UserAdmin)
