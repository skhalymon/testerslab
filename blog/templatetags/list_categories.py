from django import template

register = template.Library()


from blog.models import Category


def get_categories():
    categories = Category.objects.all()
    return {'categories': categories}

register.inclusion_tag('nav_category.html')(get_categories)
