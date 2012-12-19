from django import template

register = template.Library()


from blog.models import QuickLink


def get_quicklinks():
    quick_links = QuickLink.objects.filter(visible=True).order_by('?')
    return {'quick_links': quick_links}

register.inclusion_tag('list_quicklinks.html')(get_quicklinks)
