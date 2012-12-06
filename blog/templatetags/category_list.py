from django import template

register = template.Library()


from blog.models import Category


def nav_categorylist():
    categories = Category.objects.all()
    return {'categories': categories}

register.inclusion_tag('nav_category_list.html')(nav_categorylist)
