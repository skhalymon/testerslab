from django import template

register = template.Library()


from django.contrib.auth.models import User


def get_users():
    users = User.objects.all().order_by('?')
    return {
        'users': users,
    }

register.inclusion_tag('list_members.html')(get_users)
