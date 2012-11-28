from django.contrib import admin
from blog.models import Post, Category


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
