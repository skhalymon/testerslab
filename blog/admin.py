from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from blog.models import Category, Post, QuickLink
from blog.models import UserProfile


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created', 'get_categories', 'published')
    list_filter = ['created', 'categories']
    search_fields = ['title']
    date_hierarchy = 'created'


class QuickLinkAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'visible')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(QuickLink, QuickLinkAdmin)


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
