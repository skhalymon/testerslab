from django.contrib import admin
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'get_categories', 'is_published')
    list_filter = ['created', 'categories']
    search_fields = ['title']
    date_hierarchy = 'created'


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
