from django import template
from ..models import Person
register = template.Library()


@register.simple_tag
def person_post():
    return Person.objects.all().order_by('-id')[:3]
